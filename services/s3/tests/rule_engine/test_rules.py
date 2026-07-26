import pytest
from capo_s3._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_s3._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_region_is_not_a_valid_dns_suffix():
    """region is not a valid DNS-suffix"""
    params = EndpointParams(Region='a b', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_invalid_access_point_arn__not_s3():
    """Invalid access point ARN: Not S3"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:not-s3:us-west-2:123456789012:accesspoint:myendpoint')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN was not for the S3 service, found: not-s3')):
        resolve(params)

def test_invalid_access_point_arn__invalid_resour():
    """Invalid access point ARN: invalid resource"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint:more-data')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN may only contain a single resource component after `accesspoint`.')):
        resolve(params)

def test_invalid_access_point_arn__invalid_no_ap_():
    """Invalid access point ARN: invalid no ap name"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a resource of the format `accesspoint:<accesspoint name>` but no name was provided')):
        resolve(params)

def test_invalid_access_point_arn__accountid_is_i():
    """Invalid access point ARN: AccountId is invalid"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456_789012:accesspoint:apname')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `123456_789012`')):
        resolve(params)

def test_invalid_access_point_arn__access_point_n():
    """Invalid access point ARN: access point name is invalid"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:ap_name')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `ap_name`')):
        resolve(params)

def test_access_points__disable_access_points_exp():
    """Access points (disable access points explicitly false)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableAccessPoints=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint')
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.us-west-2.amazonaws.com'

def test_access_points__partition_does_not_suppor():
    """Access points: partition does not support FIPS"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3:cn-north-1:123456789012:accesspoint:myendpoint')
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_bucket_region_is_invalid():
    """Bucket region is invalid"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableAccessPoints=False, Bucket='arn:aws:s3:us-west -2:123456789012:accesspoint:myendpoint')
    with pytest.raises(EndpointError, match=re.escape('Invalid region in ARN: `us-west -2` (invalid DNS name)')):
        resolve(params)

def test_access_points_when_access_points_explici():
    """Access points when Access points explicitly disabled (used for CreateBucket)"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableAccessPoints=True, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint')
    with pytest.raises(EndpointError, match=re.escape('Access points are not supported for this operation')):
        resolve(params)

def test_missing_arn_type():
    """missing arn type"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableAccessPoints=True, Bucket='arn:aws:s3:us-west-2:123456789012:')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: `arn:aws:s3:us-west-2:123456789012:` was not a valid ARN')):
        resolve(params)

def test_sdk__host___access_point___dualstack_is_():
    """SDK::Host + access point + Dualstack is an error"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Endpoint='https://beta.example.com', Region='cn-north-1', UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_access_point_arn_with_fips___dualstack():
    """Access point ARN with FIPS & Dualstack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableAccessPoints=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint')
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint-fips.dualstack.us-west-2.amazonaws.com'

def test_access_point_arn_with_dualstack():
    """Access point ARN with Dualstack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableAccessPoints=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint')
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.dualstack.us-west-2.amazonaws.com'

def test_vanilla_mrap():
    """vanilla MRAP"""
    params = EndpointParams(Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-east-1', DisableMultiRegionAccessPoints=False, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://mfzwi23gnjvgw.mrap.accesspoint.s3-global.amazonaws.com'

def test_mrap_does_not_support_fips():
    """MRAP does not support FIPS"""
    params = EndpointParams(Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-east-1', DisableMultiRegionAccessPoints=False, UseFIPS=True, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('S3 MRAP does not support FIPS')):
        resolve(params)

def test_mrap_does_not_support_dualstack():
    """MRAP does not support DualStack"""
    params = EndpointParams(Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-east-1', DisableMultiRegionAccessPoints=False, UseFIPS=False, UseDualStack=True, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('S3 MRAP does not support dual-stack')):
        resolve(params)

def test_mrap_does_not_support_s3_accelerate():
    """MRAP does not support S3 Accelerate"""
    params = EndpointParams(Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-east-1', DisableMultiRegionAccessPoints=False, UseFIPS=False, UseDualStack=False, Accelerate=True)
    with pytest.raises(EndpointError, match=re.escape('S3 MRAP does not support S3 Accelerate')):
        resolve(params)

def test_mrap_explicitly_disabled():
    """MRAP explicitly disabled"""
    params = EndpointParams(Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-east-1', DisableMultiRegionAccessPoints=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: Multi-Region Access Point ARNs are disabled.')):
        resolve(params)

def test_dual_stack_endpoint_with_path_style_forc():
    """Dual-stack endpoint with path-style forced"""
    params = EndpointParams(Bucket='bucketname', Region='us-west-2', ForcePathStyle=True, UseFIPS=False, Accelerate=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-west-2.amazonaws.com/bucketname'

def test_dual_stack_endpoint___sdk__host_is_error():
    """Dual-stack endpoint + SDK::Host is error"""
    params = EndpointParams(Bucket='bucketname', Region='us-west-2', ForcePathStyle=True, UseFIPS=False, Accelerate=False, UseDualStack=True, Endpoint='https://abc.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_path_style___arn_bucket():
    """path style + ARN bucket"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', ForcePathStyle=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with ARN buckets')):
        resolve(params)

def test_implicit_path_style_bucket___dualstack():
    """implicit path style bucket + dualstack"""
    params = EndpointParams(Accelerate=False, Bucket='99_ab', Region='us-west-2', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-west-2.amazonaws.com/99_ab'

def test_implicit_path_style_bucket___dualstack():
    """implicit path style bucket + dualstack"""
    params = EndpointParams(Accelerate=False, Bucket='99_ab', Region='us-west-2', UseDualStack=True, UseFIPS=False, Endpoint='http://abc.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_don_t_allow_url_injections_in_the_bucket():
    """don't allow URL injections in the bucket"""
    params = EndpointParams(Bucket='example.com#', Region='us-west-2', UseDualStack=False, UseFIPS=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/example.com%23'

def test_uri_encode_bucket_names_in_the_path():
    """URI encode bucket names in the path"""
    params = EndpointParams(Bucket='bucket name', Region='us-west-2', UseDualStack=False, UseFIPS=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/bucket%20name'

def test_scheme_is_respected():
    """scheme is respected"""
    params = EndpointParams(Accelerate=False, Bucket='99_ab', Endpoint='http://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'http://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/99_ab'

def test_scheme_is_respected__virtual_addressing_():
    """scheme is respected (virtual addressing)"""
    params = EndpointParams(Accelerate=False, Bucket='bucketname', Endpoint='http://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/foo', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'http://bucketname.control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/foo'

def test_path_style___implicit_private_link():
    """path style + implicit private link"""
    params = EndpointParams(Accelerate=False, Bucket='99_ab', Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/99_ab'

def test_invalid_endpoint_override():
    """invalid Endpoint override"""
    params = EndpointParams(Accelerate=False, Bucket='bucketname', Endpoint='abcde://nota#url', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Custom endpoint `abcde://nota#url` was not a valid URI')):
        resolve(params)

def test_using_an_ipv4_address_forces_path_style():
    """using an IPv4 address forces path style"""
    params = EndpointParams(Accelerate=False, Bucket='bucketname', Endpoint='https://123.123.0.1', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://123.123.0.1/bucketname'

def test_vanilla_access_point_arn_with_region_mis():
    """vanilla access point arn with region mismatch and UseArnRegion=false"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-east-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, UseArnRegion=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_vanilla_access_point_arn_with_region_mis():
    """vanilla access point arn with region mismatch and UseArnRegion unset"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='us-east-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.us-west-2.amazonaws.com'

def test_vanilla_access_point_arn_with_region_mis():
    """vanilla access point arn with region mismatch and UseArnRegion=true"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, UseArnRegion=True, Region='us-east-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.us-west-2.amazonaws.com'

def test_subdomains_are_not_allowed_in_virtual_bu():
    """subdomains are not allowed in virtual buckets"""
    params = EndpointParams(Bucket='bucket.name', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://s3.us-east-1.amazonaws.com/bucket.name'

def test_bucket_names_with_3_characters_are_allow():
    """bucket names with 3 characters are allowed in virtual buckets"""
    params = EndpointParams(Bucket='aaa', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://aaa.s3.us-east-1.amazonaws.com'

def test_bucket_names_with_fewer_than_3_character():
    """bucket names with fewer than 3 characters are not allowed in virtual host"""
    params = EndpointParams(Bucket='aa', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://s3.us-east-1.amazonaws.com/aa'

def test_bucket_names_with_uppercase_characters_a():
    """bucket names with uppercase characters are not allowed in virtual host"""
    params = EndpointParams(Bucket='BucketName', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://s3.us-east-1.amazonaws.com/BucketName'

def test_subdomains_are_allowed_in_virtual_bucket():
    """subdomains are allowed in virtual buckets on http endpoints"""
    params = EndpointParams(Bucket='bucket.name', Region='us-east-1', Endpoint='http://example.com')
    result = resolve(params)
    assert result.url == 'http://bucket.name.example.com'

def test_no_region_set():
    """no region set"""
    params = EndpointParams(Bucket='bucket-name')
    with pytest.raises(EndpointError, match=re.escape('A region must be set when sending requests to S3.')):
        resolve(params)

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1 uses the global endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com'

def test_useglobalendpoints_true__region_us_west_():
    """UseGlobalEndpoints=true, region=us-west-2 uses the regional endpoint"""
    params = EndpointParams(Region='us-west-2', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com'

def test_useglobalendpoints_true__region_cn_north():
    """UseGlobalEndpoints=true, region=cn-north-1 uses the regional endpoint"""
    params = EndpointParams(Region='cn-north-1', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.cn-north-1.amazonaws.com.cn'

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1, fips=true uses the regional endpoint with fips"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=True, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com'

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1, dualstack=true uses the regional endpoint with dualstack"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com'

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1, dualstack and fips uses the regional endpoint with fips/dualstack"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=True, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com'

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1 with custom endpoint, uses custom"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_useglobalendpoints_true__region_us_west_():
    """UseGlobalEndpoints=true, region=us-west-2 with custom endpoint, uses custom"""
    params = EndpointParams(Region='us-west-2', Endpoint='https://example.com', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_useglobalendpoints_true__region_us_east_():
    """UseGlobalEndpoints=true, region=us-east-1 with accelerate on non bucket case uses the global endpoint and ignores accelerate"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=True)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com'

def test_aws_global_region_uses_the_global_endpoi():
    """aws-global region uses the global endpoint"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com'

def test_aws_global_region_with_fips_uses_the_reg():
    """aws-global region with fips uses the regional endpoint"""
    params = EndpointParams(Region='aws-global', UseFIPS=True, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com'

def test_aws_global_region_with_dualstack_uses_th():
    """aws-global region with dualstack uses the regional endpoint"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com'

def test_aws_global_region_with_fips_and_dualstac():
    """aws-global region with fips and dualstack uses the regional endpoint"""
    params = EndpointParams(Region='aws-global', UseFIPS=True, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com'

def test_aws_global_region_with_accelerate_on_non():
    """aws-global region with accelerate on non-bucket case, uses global endpoint and ignores accelerate"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False, Accelerate=True)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com'

def test_aws_global_region_with_custom_endpoint__():
    """aws-global region with custom endpoint, uses custom"""
    params = EndpointParams(Region='aws-global', Endpoint='https://example.com', UseGlobalEndpoint=False, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_virtual_addressing__aws_global_region_us():
    """virtual addressing, aws-global region uses the global endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with Prefix, and Key uses the global endpoint. Prefix and Key parameters should not be used in endpoint evaluation."""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False, Prefix='prefix', Key='key')
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with Copy Source, and Key uses the global endpoint. Copy Source and Key parameters should not be used in endpoint evaluation."""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False, CopySource='/copy/source', Key='key')
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with fips uses the regional fips endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=True, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.us-east-1.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with dualstack uses the regional dualstack endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.dualstack.us-east-1.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with fips/dualstack uses the regional fips/dualstack endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=True, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.dualstack.us-east-1.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with accelerate uses the global accelerate endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.amazonaws.com'

def test_virtual_addressing__aws_global_region_wi():
    """virtual addressing, aws-global region with custom endpoint"""
    params = EndpointParams(Region='aws-global', Endpoint='https://example.com', Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.example.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-east-1 region uses the global endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.amazonaws.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-west-2 region uses the regional endpoint"""
    params = EndpointParams(Region='us-west-2', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.us-west-2.amazonaws.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-east-1 region and fips uses the regional fips endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=True, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.us-east-1.amazonaws.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-east-1 region and dualstack uses the regional dualstack endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.dualstack.us-east-1.amazonaws.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-east-1 region and accelerate uses the global accelerate endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.amazonaws.com'

def test_virtual_addressing__useglobalendpoint_an():
    """virtual addressing, UseGlobalEndpoint and us-east-1 region with custom endpoint"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseGlobalEndpoint=True, Bucket='bucket-name', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.example.com'

def test_forcepathstyle__aws_global_region_uses_t():
    """ForcePathStyle, aws-global region uses the global endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', ForcePathStyle=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com/bucket-name'

def test_forcepathstyle__aws_global_region_with_f():
    """ForcePathStyle, aws-global region with fips is invalid"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', ForcePathStyle=True, UseFIPS=True, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com/bucket-name'

def test_forcepathstyle__aws_global_region_with_d():
    """ForcePathStyle, aws-global region with dualstack uses regional dualstack endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket-name', ForcePathStyle=True, UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com/bucket-name'

def test_forcepathstyle__aws_global_region_custom():
    """ForcePathStyle, aws-global region custom endpoint uses the custom endpoint"""
    params = EndpointParams(Region='aws-global', Endpoint='https://example.com', Bucket='bucket-name', ForcePathStyle=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://example.com/bucket-name'

def test_forcepathstyle__useglobalendpoint_us_eas():
    """ForcePathStyle, UseGlobalEndpoint us-east-1 region uses the global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket-name', UseGlobalEndpoint=True, ForcePathStyle=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com/bucket-name'

def test_forcepathstyle__useglobalendpoint_us_wes():
    """ForcePathStyle, UseGlobalEndpoint us-west-2 region uses the regional endpoint"""
    params = EndpointParams(Region='us-west-2', Bucket='bucket-name', UseGlobalEndpoint=True, ForcePathStyle=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/bucket-name'

def test_forcepathstyle__useglobalendpoint_us_eas():
    """ForcePathStyle, UseGlobalEndpoint us-east-1 region, dualstack uses the regional dualstack endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket-name', UseGlobalEndpoint=True, ForcePathStyle=True, UseFIPS=False, UseDualStack=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com/bucket-name'

def test_forcepathstyle__useglobalendpoint_us_eas():
    """ForcePathStyle, UseGlobalEndpoint us-east-1 region custom endpoint uses the custom endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket-name', Endpoint='https://example.com', UseGlobalEndpoint=True, ForcePathStyle=True, UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://example.com/bucket-name'

def test_arn_with_aws_global_region_and__usearnre():
    """ARN with aws-global region and  UseArnRegion uses the regional endpoint"""
    params = EndpointParams(Region='aws-global', UseArnRegion=True, UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    result = resolve(params)
    assert result.url == 'https://reports-123456789012.op-01234567890123456.s3-outposts.us-east-1.amazonaws.com'

def test_cross_partition_mrap_arn_is_an_error():
    """cross partition MRAP ARN is an error"""
    params = EndpointParams(Bucket='arn:aws-cn:s3::123456789012:accesspoint:mfzwi23gnjvgw.mrap', Region='us-west-1')
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but bucket referred to partition `aws-cn`')):
        resolve(params)

def test_endpoint_override__accesspoint_with_http():
    """Endpoint override, accesspoint with HTTP, port"""
    params = EndpointParams(Endpoint='http://beta.example.com:1234', Region='us-west-2', Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint')
    result = resolve(params)
    assert result.url == 'http://myendpoint-123456789012.beta.example.com:1234'

def test_endpoint_override__accesspoint_with_http():
    """Endpoint override, accesspoint with http, path, query, and port"""
    params = EndpointParams(Region='us-west-2', Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', Endpoint='http://beta.example.com:1234/path', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'http://myendpoint-123456789012.beta.example.com:1234/path'

def test_non_bucket_endpoint_override_with_fips__():
    """non-bucket endpoint override with FIPS = error"""
    params = EndpointParams(Region='us-west-2', Endpoint='http://beta.example.com:1234/path', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_fips___dualstack___custom_endpoint():
    """FIPS + dualstack + custom endpoint"""
    params = EndpointParams(Region='us-west-2', Endpoint='http://beta.example.com:1234/path', UseFIPS=True, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_dualstack___custom_endpoint():
    """dualstack + custom endpoint"""
    params = EndpointParams(Region='us-west-2', Endpoint='http://beta.example.com:1234/path', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_custom_endpoint_without_fips_dualstack():
    """custom endpoint without FIPS/dualstack"""
    params = EndpointParams(Region='us-west-2', Endpoint='http://beta.example.com:1234/path', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://beta.example.com:1234/path'

def test_s3_object_lambda_with_access_points_disa():
    """s3 object lambda with access points disabled"""
    params = EndpointParams(Region='us-west-2', Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint:myendpoint', DisableAccessPoints=True)
    with pytest.raises(EndpointError, match=re.escape('Access points are not supported for this operation')):
        resolve(params)

def test_non_bucket___fips():
    """non bucket + FIPS"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-west-2.amazonaws.com'

def test_standard_non_bucket_endpoint():
    """standard non bucket endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com'

def test_non_bucket_endpoint_with_fips___dualstac():
    """non bucket endpoint with FIPS + Dualstack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-west-2.amazonaws.com'

def test_non_bucket_endpoint_with_dualstack():
    """non bucket endpoint with dualstack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-west-2.amazonaws.com'

def test_use_global_endpoint___ip_address_endpoin():
    """use global endpoint + IP address endpoint override"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket', UseFIPS=False, UseDualStack=False, Endpoint='http://127.0.0.1', UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'http://127.0.0.1/bucket'

def test_non_dns_endpoint___global_endpoint():
    """non-dns endpoint + global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=False, UseDualStack=False, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com/bucket%21'

def test_endpoint_override___use_global_endpoint():
    """endpoint override + use global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=False, UseDualStack=False, UseGlobalEndpoint=True, Endpoint='http://foo.com')
    result = resolve(params)
    assert result.url == 'http://foo.com/bucket%21'

def test_fips___dualstack___non_bucket_endpoint():
    """FIPS + dualstack + non-bucket endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_fips___dualstack___non_dns_endpoint():
    """FIPS + dualstack + non-DNS endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', ForcePathStyle=True, UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_endpoint_override___fips___dualstack__bu():
    """endpoint override + FIPS + dualstack (BUG)"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', ForcePathStyle=True, UseFIPS=True, UseDualStack=False, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_endpoint_override___non_dns_bucket___fip():
    """endpoint override + non-dns bucket + FIPS (BUG)"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=True, UseDualStack=False, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_fips___bucket_endpoint___force_path_styl():
    """FIPS + bucket endpoint + force path style"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', ForcePathStyle=True, UseFIPS=True, UseDualStack=False, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com/bucket%21'

def test_bucket___fips___force_path_style():
    """bucket + FIPS + force path style"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket', ForcePathStyle=True, UseFIPS=True, UseDualStack=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket'

def test_fips___dualstack___use_global_endpoint():
    """FIPS + dualstack + use global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket', UseFIPS=True, UseDualStack=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://bucket.s3-fips.dualstack.us-east-1.amazonaws.com'

def test_uri_encoded_bucket___use_global_endpoint():
    """URI encoded bucket + use global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=True, UseDualStack=False, UseGlobalEndpoint=True, Endpoint='https://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_fips___path_based_endpoint():
    """FIPS + path based endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', UseFIPS=True, UseDualStack=False, Accelerate=False, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com/bucket%21'

def test_accelerate___dualstack___global_endpoint():
    """accelerate + dualstack + global endpoint"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket', UseFIPS=False, UseDualStack=True, Accelerate=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://bucket.s3-accelerate.dualstack.amazonaws.com'

def test_dualstack___global_endpoint___non_uri_sa():
    """dualstack + global endpoint + non URI safe bucket"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', Accelerate=False, UseDualStack=True, UseFIPS=False, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_fips___uri_encoded_bucket():
    """FIPS + uri encoded bucket"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', ForcePathStyle=True, Accelerate=False, UseDualStack=False, UseFIPS=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com/bucket%21'

def test_endpoint_override___non_uri_safe_endpoin():
    """endpoint override + non-uri safe endpoint + force path style"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', ForcePathStyle=True, Accelerate=False, UseDualStack=False, UseFIPS=True, Endpoint='http://foo.com', UseGlobalEndpoint=True)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_fips___dualstack___global_endpoint___non():
    """FIPS + Dualstack + global endpoint + non-dns bucket"""
    params = EndpointParams(Region='us-east-1', Bucket='bucket!', Accelerate=False, UseDualStack=True, UseFIPS=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_endpoint_override___fips___dualstack():
    """endpoint override + FIPS + dualstack"""
    params = EndpointParams(Region='us-east-1', UseDualStack=True, UseFIPS=True, UseGlobalEndpoint=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_non_bucket_endpoint_override___dualstack():
    """non-bucket endpoint override + dualstack + global endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, UseGlobalEndpoint=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_endpoint_override___useglobalendpoint___():
    """Endpoint override + UseGlobalEndpoint + us-east-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, UseGlobalEndpoint=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_non_fips_partition_with_fips_set___custo():
    """non-FIPS partition with FIPS set + custom endpoint"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False, UseGlobalEndpoint=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_aws_global_signs_as_us_east_1():
    """aws-global signs as us-east-1"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', UseFIPS=True, Accelerate=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_aws_global_signs_as_us_east_1():
    """aws-global signs as us-east-1"""
    params = EndpointParams(Region='aws-global', Bucket='bucket', UseDualStack=False, UseFIPS=False, Accelerate=False, Endpoint='https://foo.com')
    result = resolve(params)
    assert result.url == 'https://bucket.foo.com'

def test_aws_global___dualstack___path_only_bucke():
    """aws-global + dualstack + path-only bucket"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', UseDualStack=True, UseFIPS=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_aws_global___path_only_bucket():
    """aws-global + path-only bucket"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!')
    result = resolve(params)
    assert result.url == 'https://s3.amazonaws.com/bucket%21'

def test_aws_global___fips___custom_endpoint():
    """aws-global + fips + custom endpoint"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', UseDualStack=False, UseFIPS=True, Accelerate=False, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_aws_global__endpoint_override___path_onl():
    """aws-global, endpoint override & path only-bucket"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', UseDualStack=False, UseFIPS=False, Accelerate=False, Endpoint='http://foo.com')
    result = resolve(params)
    assert result.url == 'http://foo.com/bucket%21'

def test_aws_global___dualstack___custom_endpoint():
    """aws-global + dualstack + custom endpoint"""
    params = EndpointParams(Region='aws-global', UseDualStack=True, UseFIPS=False, Accelerate=False, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_accelerate__dualstack___aws_global():
    """accelerate, dualstack + aws-global"""
    params = EndpointParams(Region='aws-global', Bucket='bucket', UseDualStack=True, UseFIPS=False, Accelerate=True)
    result = resolve(params)
    assert result.url == 'https://bucket.s3-accelerate.dualstack.us-east-1.amazonaws.com'

def test_fips___aws_global___path_only_bucket__th():
    """FIPS + aws-global + path only bucket. This is not supported by S3 but we allow garbage in garbage out"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', ForcePathStyle=True, UseDualStack=True, UseFIPS=True, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://s3-fips.dualstack.us-east-1.amazonaws.com/bucket%21'

def test_aws_global___fips___endpoint_override_():
    """aws-global + FIPS + endpoint override."""
    params = EndpointParams(Region='aws-global', UseFIPS=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_force_path_style__fips__aws_global___end():
    """force path style, FIPS, aws-global & endpoint override"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', ForcePathStyle=True, UseFIPS=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_ip_address_causes_path_style_to_be_force():
    """ip address causes path style to be forced"""
    params = EndpointParams(Region='aws-global', Bucket='bucket', Endpoint='http://192.168.1.1')
    result = resolve(params)
    assert result.url == 'http://192.168.1.1/bucket'

def test_endpoint_override_with_aws_global_region():
    """endpoint override with aws-global region"""
    params = EndpointParams(Region='aws-global', UseFIPS=True, UseDualStack=True, Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_fips___path_only__todo__consider_making_():
    """FIPS + path-only (TODO: consider making this an error)"""
    params = EndpointParams(Region='aws-global', Bucket='bucket!', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-east-1.amazonaws.com/bucket%21'

def test_empty_arn_type():
    """empty arn type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:not-s3:us-west-2:123456789012::myendpoint')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: No ARN type specified')):
        resolve(params)

def test_path_style_can_t_be_used_with_accelerate():
    """path style can't be used with accelerate"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket!', Accelerate=True)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with S3 Accelerate')):
        resolve(params)

def test_invalid_region():
    """invalid region"""
    params = EndpointParams(Region='us-east-2!', Bucket='bucket.subdomain', Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_invalid_region():
    """invalid region"""
    params = EndpointParams(Region='us-east-2!', Bucket='bucket', Endpoint='http://foo.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_empty_arn_type():
    """empty arn type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3::123456789012:accesspoint:my_endpoint')
    with pytest.raises(EndpointError, match=re.escape('Invalid Access Point Name')):
        resolve(params)

def test_empty_arn_type():
    """empty arn type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3:cn-north-1:123456789012:accesspoint:my-endpoint', UseArnRegion=True)
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but ARN (`arn:aws:s3:cn-north-1:123456789012:accesspoint:my-endpoint`) has `aws-cn`')):
        resolve(params)

def test_invalid_arn_region():
    """invalid arn region"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-object-lambda:us-east_2:123456789012:accesspoint:my-endpoint', UseArnRegion=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid region in ARN: `us-east_2` (invalid DNS name)')):
        resolve(params)

def test_invalid_arn_outpost():
    """invalid ARN outpost"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op_01234567890123456/accesspoint/reports', UseArnRegion=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The outpost Id may only contain a-z, A-Z, 0-9 and `-`. Found: `op_01234567890123456`')):
        resolve(params)

def test_invalid_arn():
    """invalid ARN"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-01234567890123456/reports')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: expected an access point name')):
        resolve(params)

def test_invalid_arn():
    """invalid ARN"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-01234567890123456')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a 4-component resource')):
        resolve(params)

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-01234567890123456/not-accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('Expected an outpost type `accesspoint`, found not-accesspoint')):
        resolve(params)

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east_1:123456789012:outpost/op-01234567890123456/not-accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('Invalid region in ARN: `us-east_1` (invalid DNS name)')):
        resolve(params)

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:12345_789012:outpost/op-01234567890123456/not-accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `12345_789012`')):
        resolve(params)

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='arn:aws:s3-outposts:us-east-1:12345789012:outpost')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The Outpost Id was not set')):
        resolve(params)

def test_use_global_endpoint_virtual_addressing():
    """use global endpoint virtual addressing"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket', Endpoint='http://example.com', UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'http://bucket.example.com'

def test_global_endpoint___ip_address():
    """global endpoint + ip address"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket', Endpoint='http://192.168.0.1', UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'http://192.168.0.1/bucket'

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket!', UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3.us-east-2.amazonaws.com/bucket%21'

def test_invalid_outpost_type():
    """invalid outpost type"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket', Accelerate=True, UseGlobalEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://bucket.s3-accelerate.amazonaws.com'

def test_use_global_endpoint___custom_endpoint():
    """use global endpoint + custom endpoint"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket!', UseGlobalEndpoint=True, Endpoint='http://foo.com')
    result = resolve(params)
    assert result.url == 'http://foo.com/bucket%21'

def test_use_global_endpoint__not_us_east_1__forc():
    """use global endpoint, not us-east-1, force path style"""
    params = EndpointParams(Region='us-east-2', Bucket='bucket!', UseGlobalEndpoint=True, ForcePathStyle=True, Endpoint='http://foo.com')
    result = resolve(params)
    assert result.url == 'http://foo.com/bucket%21'

def test_vanilla_virtual_addressing_us_west_2():
    """vanilla virtual addressing@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.us-west-2.amazonaws.com'

def test_virtual_addressing___dualstack_us_west_2():
    """virtual addressing + dualstack@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.dualstack.us-west-2.amazonaws.com'

def test_accelerate___dualstack_us_west_2():
    """accelerate + dualstack@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.dualstack.amazonaws.com'

def test_accelerate__dualstack_false__us_west_2():
    """accelerate (dualstack=false)@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.amazonaws.com'

def test_virtual_addressing___fips_us_west_2():
    """virtual addressing + fips@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.us-west-2.amazonaws.com'

def test_virtual_addressing___dualstack___fips_us():
    """virtual addressing + dualstack + fips@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.dualstack.us-west-2.amazonaws.com'

def test_accelerate___fips___error_us_west_2():
    """accelerate + fips = error@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Accelerate cannot be used with FIPS')):
        resolve(params)

def test_vanilla_virtual_addressing_cn_north_1():
    """vanilla virtual addressing@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.cn-north-1.amazonaws.com.cn'

def test_virtual_addressing___dualstack_cn_north_():
    """virtual addressing + dualstack@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='cn-north-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.dualstack.cn-north-1.amazonaws.com.cn'

def test_accelerate__dualstack_false__cn_north_1():
    """accelerate (dualstack=false)@cn-north-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('S3 Accelerate cannot be used in this region')):
        resolve(params)

def test_virtual_addressing___fips_cn_north_1():
    """virtual addressing + fips@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_vanilla_virtual_addressing_af_south_1():
    """vanilla virtual addressing@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.af-south-1.amazonaws.com'

def test_virtual_addressing___dualstack_af_south_():
    """virtual addressing + dualstack@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3.dualstack.af-south-1.amazonaws.com'

def test_accelerate___dualstack_af_south_1():
    """accelerate + dualstack@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.dualstack.amazonaws.com'

def test_accelerate__dualstack_false__af_south_1():
    """accelerate (dualstack=false)@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-accelerate.amazonaws.com'

def test_virtual_addressing___fips_af_south_1():
    """virtual addressing + fips@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.af-south-1.amazonaws.com'

def test_virtual_addressing___dualstack___fips_af():
    """virtual addressing + dualstack + fips@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://bucket-name.s3-fips.dualstack.af-south-1.amazonaws.com'

def test_accelerate___fips___error_af_south_1():
    """accelerate + fips = error@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Accelerate cannot be used with FIPS')):
        resolve(params)

def test_vanilla_path_style_us_west_2():
    """vanilla path style@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/bucket-name'

def test_fips_us_gov_west_2__bucket_is_not_s3_dns():
    """fips@us-gov-west-2, bucket is not S3-dns-compatible (subdomains)"""
    params = EndpointParams(Accelerate=False, Bucket='bucket.with.dots', Region='us-gov-west-1', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.us-gov-west-1.amazonaws.com/bucket.with.dots'

def test_path_style___accelerate___error_us_west_():
    """path style + accelerate = error@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with S3 Accelerate')):
        resolve(params)

def test_path_style___dualstack_us_west_2():
    """path style + dualstack@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='us-west-2', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.us-west-2.amazonaws.com/bucket-name'

def test_path_style___arn_is_error_us_west_2():
    """path style + arn is error@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='arn:PARTITION:s3-outposts:REGION:123456789012:outpost:op-01234567890123456:bucket:mybucket', ForcePathStyle=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with ARN buckets')):
        resolve(params)

def test_path_style___invalid_dns_name_us_west_2():
    """path style + invalid DNS name@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', ForcePathStyle=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/99a_b'

def test_no_path_style___invalid_dns_name_us_west():
    """no path style + invalid DNS name@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.us-west-2.amazonaws.com/99a_b'

def test_vanilla_path_style_cn_north_1():
    """vanilla path style@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.cn-north-1.amazonaws.com.cn/bucket-name'

def test_path_style___fips_cn_north_1():
    """path style + fips@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='cn-north-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_path_style___accelerate___error_cn_north():
    """path style + accelerate = error@cn-north-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=True, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with S3 Accelerate')):
        resolve(params)

def test_path_style___dualstack_cn_north_1():
    """path style + dualstack@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='cn-north-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.cn-north-1.amazonaws.com.cn/bucket-name'

def test_path_style___arn_is_error_cn_north_1():
    """path style + arn is error@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:PARTITION:s3-outposts:REGION:123456789012:outpost:op-01234567890123456:bucket:mybucket', ForcePathStyle=True, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with ARN buckets')):
        resolve(params)

def test_path_style___invalid_dns_name_cn_north_1():
    """path style + invalid DNS name@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', ForcePathStyle=True, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.cn-north-1.amazonaws.com.cn/99a_b'

def test_no_path_style___invalid_dns_name_cn_nort():
    """no path style + invalid DNS name@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.cn-north-1.amazonaws.com.cn/99a_b'

def test_vanilla_path_style_af_south_1():
    """vanilla path style@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.af-south-1.amazonaws.com/bucket-name'

def test_path_style___fips_af_south_1():
    """path style + fips@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='af-south-1', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-fips.af-south-1.amazonaws.com/bucket-name'

def test_path_style___accelerate___error_af_south():
    """path style + accelerate = error@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=True, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with S3 Accelerate')):
        resolve(params)

def test_path_style___dualstack_af_south_1():
    """path style + dualstack@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Region='af-south-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.dualstack.af-south-1.amazonaws.com/bucket-name'

def test_path_style___arn_is_error_af_south_1():
    """path style + arn is error@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:PARTITION:s3-outposts:REGION:123456789012:outpost:op-01234567890123456:bucket:mybucket', ForcePathStyle=True, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Path-style addressing cannot be used with ARN buckets')):
        resolve(params)

def test_path_style___invalid_dns_name_af_south_1():
    """path style + invalid DNS name@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', ForcePathStyle=True, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.af-south-1.amazonaws.com/99a_b'

def test_no_path_style___invalid_dns_name_af_sout():
    """no path style + invalid DNS name@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='99a_b', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3.af-south-1.amazonaws.com/99a_b'

def test_virtual_addressing___private_link_us_wes():
    """virtual addressing + private link@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='http://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'http://bucket-name.control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com'

def test_path_style___private_link_us_west_2():
    """path style + private link@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/bucket-name'

def test_sdk__host___fips_us_west_2():
    """SDK::Host + FIPS@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_sdk__host___dualstack_us_west_2():
    """SDK::Host + DualStack@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_sdk__host___accelerate_us_west_2():
    """SDK::HOST + accelerate@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Endpoint='http://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with S3 Accelerate')):
        resolve(params)

def test_sdk__host___access_point_arn_us_west_2():
    """SDK::Host + access point ARN@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Endpoint='https://beta.example.com', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.beta.example.com'

def test_virtual_addressing___private_link_cn_nor():
    """virtual addressing + private link@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com'

def test_path_style___private_link_cn_north_1():
    """path style + private link@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/bucket-name'

def test_fips_cn_north_1():
    """FIPS@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_sdk__host___dualstack_cn_north_1():
    """SDK::Host + DualStack@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='cn-north-1', UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_sdk__host___accelerate_cn_north_1():
    """SDK::HOST + accelerate@cn-north-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with S3 Accelerate')):
        resolve(params)

def test_sdk__host___access_point_arn_cn_north_1():
    """SDK::Host + access point ARN@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Endpoint='https://beta.example.com', Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.beta.example.com'

def test_virtual_addressing___private_link_af_sou():
    """virtual addressing + private link@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://bucket-name.control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com'

def test_path_style___private_link_af_south_1():
    """path style + private link@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=True, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com/bucket-name'

def test_sdk__host___fips_af_south_1():
    """SDK::Host + FIPS@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with FIPS')):
        resolve(params)

def test_sdk__host___dualstack_af_south_1():
    """SDK::Host + DualStack@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Cannot set dual-stack in combination with a custom endpoint.')):
        resolve(params)

def test_sdk__host___accelerate_af_south_1():
    """SDK::HOST + accelerate@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='bucket-name', ForcePathStyle=False, Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('A custom endpoint cannot be combined with S3 Accelerate')):
        resolve(params)

def test_sdk__host___access_point_arn_af_south_1():
    """SDK::Host + access point ARN@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:af-south-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Endpoint='https://beta.example.com', Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.beta.example.com'

def test_vanilla_access_point_arn_us_west_2():
    """vanilla access point arn@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.us-west-2.amazonaws.com'

def test_access_point_arn___fips_us_west_2():
    """access point arn + FIPS@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint-fips.us-west-2.amazonaws.com'

def test_access_point_arn___accelerate___error_us():
    """access point arn + accelerate = error@us-west-2"""
    params = EndpointParams(Accelerate=True, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Access Points do not support S3 Accelerate')):
        resolve(params)

def test_access_point_arn___fips___dualstack_us_w():
    """access point arn + FIPS + DualStack@us-west-2"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:us-west-2:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='us-west-2', UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint-fips.dualstack.us-west-2.amazonaws.com'

def test_vanilla_access_point_arn_cn_north_1():
    """vanilla access point arn@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.cn-north-1.amazonaws.com.cn'

def test_access_point_arn___fips_cn_north_1():
    """access point arn + FIPS@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_access_point_arn___accelerate___error_cn():
    """access point arn + accelerate = error@cn-north-1"""
    params = EndpointParams(Accelerate=True, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='cn-north-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Access Points do not support S3 Accelerate')):
        resolve(params)

def test_access_point_arn___fips___dualstack_cn_n():
    """access point arn + FIPS + DualStack@cn-north-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws-cn:s3:cn-north-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='cn-north-1', UseDualStack=True, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_vanilla_access_point_arn_af_south_1():
    """vanilla access point arn@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:af-south-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint.af-south-1.amazonaws.com'

def test_access_point_arn___fips_af_south_1():
    """access point arn + FIPS@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:af-south-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint-fips.af-south-1.amazonaws.com'

def test_access_point_arn___accelerate___error_af():
    """access point arn + accelerate = error@af-south-1"""
    params = EndpointParams(Accelerate=True, Bucket='arn:aws:s3:af-south-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='af-south-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Access Points do not support S3 Accelerate')):
        resolve(params)

def test_access_point_arn___fips___dualstack_af_s():
    """access point arn + FIPS + DualStack@af-south-1"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3:af-south-1:123456789012:accesspoint:myendpoint', ForcePathStyle=False, Region='af-south-1', UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://myendpoint-123456789012.s3-accesspoint-fips.dualstack.af-south-1.amazonaws.com'

def test_s3_outposts_vanilla_test():
    """S3 outposts vanilla test"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    result = resolve(params)
    assert result.url == 'https://reports-123456789012.op-01234567890123456.s3-outposts.us-west-2.amazonaws.com'

def test_s3_outposts_custom_endpoint():
    """S3 outposts custom endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost/op-01234567890123456/accesspoint/reports', Endpoint='https://example.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://reports-123456789012.op-01234567890123456.example.amazonaws.com'

def test_outposts_arn_with_region_mismatch_and_us():
    """outposts arn with region mismatch and UseArnRegion=false"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', ForcePathStyle=False, UseArnRegion=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_outposts_arn_with_region_mismatch__custo():
    """outposts arn with region mismatch, custom region and UseArnRegion=false"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', Endpoint='https://example.com', ForcePathStyle=False, UseArnRegion=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_outposts_arn_with_region_mismatch_and_us():
    """outposts arn with region mismatch and UseArnRegion=true"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', ForcePathStyle=False, UseArnRegion=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint-123456789012.op-01234567890123456.s3-outposts.us-east-1.amazonaws.com'

def test_outposts_arn_with_region_mismatch_and_us():
    """outposts arn with region mismatch and UseArnRegion unset"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', ForcePathStyle=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint-123456789012.op-01234567890123456.s3-outposts.us-east-1.amazonaws.com'

def test_outposts_arn_with_partition_mismatch_and():
    """outposts arn with partition mismatch and UseArnRegion=true"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', ForcePathStyle=False, UseArnRegion=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but ARN (`arn:aws:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint`) has `aws-cn`')):
        resolve(params)

def test_arn_with_useglobalendpoint_and_use_east_():
    """ARN with UseGlobalEndpoint and use-east-1 region uses the regional endpoint"""
    params = EndpointParams(Region='us-east-1', UseGlobalEndpoint=True, UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    result = resolve(params)
    assert result.url == 'https://reports-123456789012.op-01234567890123456.s3-outposts.us-east-1.amazonaws.com'

def test_s3_outposts_does_not_support_dualstack():
    """S3 outposts does not support dualstack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('S3 Outposts does not support Dual-stack')):
        resolve(params)

def test_s3_outposts_does_not_support_fips():
    """S3 outposts does not support fips"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('S3 Outposts does not support FIPS')):
        resolve(params)

def test_s3_outposts_does_not_support_accelerate():
    """S3 outposts does not support accelerate"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=True, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost/op-01234567890123456/accesspoint/reports')
    with pytest.raises(EndpointError, match=re.escape('S3 Outposts does not support S3 Accelerate')):
        resolve(params)

def test_validates_against_subresource():
    """validates against subresource"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:mybucket:object:foo')
    with pytest.raises(EndpointError, match=re.escape('Invalid Arn: Outpost Access Point ARN contains sub resources')):
        resolve(params)

def test_validates_against_access_point_host_labe():
    """validates against access point host label"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:invalid.bucket#')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `invalid.bucket#`')):
        resolve(params)

def test_object_lambda__us_east_1():
    """object lambda @us-east-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-east-1.amazonaws.com'

def test_object_lambda__us_west_2():
    """object lambda @us-west-2"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-west-2.amazonaws.com'

def test_object_lambda__colon_resource_deliminato():
    """object lambda, colon resource deliminator @us-west-2"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint:mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-west-2.amazonaws.com'

def test_object_lambda__us_east_1__client_region_():
    """object lambda @us-east-1, client region us-west-2, useArnRegion=true"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-east-1.amazonaws.com'

def test_object_lambda__us_east_1__client_region_():
    """object lambda @us-east-1, client region s3-external-1, useArnRegion=true"""
    params = EndpointParams(Region='s3-external-1', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-east-1.amazonaws.com'

def test_object_lambda__us_east_1__client_region_():
    """object lambda @us-east-1, client region s3-external-1, useArnRegion=false"""
    params = EndpointParams(Region='s3-external-1', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `s3-external-1` and UseArnRegion is `false`')):
        resolve(params)

def test_object_lambda__us_east_1__client_region_():
    """object lambda @us-east-1, client region aws-global, useArnRegion=true"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-east-1.amazonaws.com'

def test_object_lambda__us_east_1__client_region_():
    """object lambda @us-east-1, client region aws-global, useArnRegion=false"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `aws-global` and UseArnRegion is `false`')):
        resolve(params)

def test_object_lambda__cn_north_1__client_region():
    """object lambda @cn-north-1, client region us-west-2 (cross partition), useArnRegion=true"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws-cn:s3-object-lambda:cn-north-1:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but ARN (`arn:aws-cn:s3-object-lambda:cn-north-1:123456789012:accesspoint/mybanner`) has `aws-cn`')):
        resolve(params)

def test_object_lambda_with_dualstack():
    """object lambda with dualstack"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('S3 Object Lambda does not support Dual-stack')):
        resolve(params)

def test_object_lambda__us_gov_east_1():
    """object lambda @us-gov-east-1"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws-us-gov:s3-object-lambda:us-gov-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda.us-gov-east-1.amazonaws.com'

def test_object_lambda__us_gov_east_1__with_fips():
    """object lambda @us-gov-east-1, with fips"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws-us-gov:s3-object-lambda:us-gov-east-1:123456789012:accesspoint/mybanner')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.s3-object-lambda-fips.us-gov-east-1.amazonaws.com'

def test_object_lambda__cn_north_1__with_fips():
    """object lambda @cn-north-1, with fips"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws-cn:s3-object-lambda:cn-north-1:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_object_lambda_with_accelerate():
    """object lambda with accelerate"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=True, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('S3 Object Lambda does not support S3 Accelerate')):
        resolve(params)

def test_object_lambda_with_invalid_arn___bad_ser():
    """object lambda with invalid arn - bad service and someresource"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:sqs:us-west-2:123456789012:someresource')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Unrecognized format: arn:aws:sqs:us-west-2:123456789012:someresource (type: someresource)')):
        resolve(params)

def test_object_lambda_with_invalid_arn___invalid():
    """object lambda with invalid arn - invalid resource"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:bucket_name:mybucket')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Object Lambda ARNs only support `accesspoint` arn types, but found: `bucket_name`')):
        resolve(params)

def test_object_lambda_with_invalid_arn___missing():
    """object lambda with invalid arn - missing region"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda::123456789012:accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: bucket ARN is missing a region')):
        resolve(params)

def test_object_lambda_with_invalid_arn___missing():
    """object lambda with invalid arn - missing account-id"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2::accesspoint/mybanner')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Missing account id')):
        resolve(params)

def test_object_lambda_with_invalid_arn___account():
    """object lambda with invalid arn - account id contains invalid characters"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2:123.45678.9012:accesspoint:mybucket')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The account id may only contain a-z, A-Z, 0-9 and `-`. Found: `123.45678.9012`')):
        resolve(params)

def test_object_lambda_with_invalid_arn___missing():
    """object lambda with invalid arn - missing access point name"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a resource of the format `accesspoint:<accesspoint name>` but no name was provided')):
        resolve(params)

def test_object_lambda_with_invalid_arn___access_():
    """object lambda with invalid arn - access point name contains invalid character: *"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint:*')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `*`')):
        resolve(params)

def test_object_lambda_with_invalid_arn___access_():
    """object lambda with invalid arn - access point name contains invalid character: ."""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint:my.bucket')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The access point name may only contain a-z, A-Z, 0-9 and `-`. Found: `my.bucket`')):
        resolve(params)

def test_object_lambda_with_invalid_arn___access_():
    """object lambda with invalid arn - access point name contains sub resources"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=True, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint:mybucket:object:foo')
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The ARN may only contain a single resource component after `accesspoint`.')):
        resolve(params)

def test_object_lambda_with_custom_endpoint():
    """object lambda with custom endpoint"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseArnRegion=False, Bucket='arn:aws:s3-object-lambda:us-west-2:123456789012:accesspoint/mybanner', Endpoint='https://my-endpoint.com')
    result = resolve(params)
    assert result.url == 'https://mybanner-123456789012.my-endpoint.com'

def test_object_lambda_arn_with_region_mismatch_a():
    """object lambda arn with region mismatch and UseArnRegion=false"""
    params = EndpointParams(Accelerate=False, Bucket='arn:aws:s3-object-lambda:us-east-1:123456789012:accesspoint/mybanner', ForcePathStyle=False, UseArnRegion=False, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_writegetobjectresponse___us_west_2():
    """WriteGetObjectResponse @ us-west-2"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-object-lambda.us-west-2.amazonaws.com'

def test_writegetobjectresponse_with_custom_endpo():
    """WriteGetObjectResponse with custom endpoint"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Endpoint='https://my-endpoint.com', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://my-endpoint.com'

def test_writegetobjectresponse___us_east_1():
    """WriteGetObjectResponse @ us-east-1"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='us-east-1', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-object-lambda.us-east-1.amazonaws.com'

def test_writegetobjectresponse_with_fips():
    """WriteGetObjectResponse with fips"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='us-east-1', UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-object-lambda-fips.us-east-1.amazonaws.com'

def test_writegetobjectresponse_with_dualstack():
    """WriteGetObjectResponse with dualstack"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='us-east-1', UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('S3 Object Lambda does not support Dual-stack')):
        resolve(params)

def test_writegetobjectresponse_with_accelerate():
    """WriteGetObjectResponse with accelerate"""
    params = EndpointParams(Accelerate=True, UseObjectLambdaEndpoint=True, Region='us-east-1', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('S3 Object Lambda does not support S3 Accelerate')):
        resolve(params)

def test_writegetobjectresponse_with_fips_in_cn():
    """WriteGetObjectResponse with fips in CN"""
    params = EndpointParams(Accelerate=False, Region='cn-north-1', UseObjectLambdaEndpoint=True, UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_writegetobjectresponse_with_invalid_part():
    """WriteGetObjectResponse with invalid partition"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='not a valid DNS name', UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_writegetobjectresponse_with_an_unknown_p():
    """WriteGetObjectResponse with an unknown partition"""
    params = EndpointParams(Accelerate=False, UseObjectLambdaEndpoint=True, Region='us-east.special', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-object-lambda.us-east.special.amazonaws.com'

def test_s3_outposts_bucketalias_real_outpost_pro():
    """S3 Outposts bucketAlias Real Outpost Prod us-west-1"""
    params = EndpointParams(Region='us-west-1', Bucket='test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3.op-0b1d075431d83bebd.s3-outposts.us-west-1.amazonaws.com'

def test_s3_outposts_bucketalias_real_outpost_pro():
    """S3 Outposts bucketAlias Real Outpost Prod ap-east-1"""
    params = EndpointParams(Region='ap-east-1', Bucket='test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3.op-0b1d075431d83bebd.s3-outposts.ap-east-1.amazonaws.com'

def test_s3_outposts_bucketalias_ec2_outpost_prod():
    """S3 Outposts bucketAlias Ec2 Outpost Prod us-east-1"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-e0000075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://test-accessp-e0000075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3.ec2.s3-outposts.us-east-1.amazonaws.com'

def test_s3_outposts_bucketalias_ec2_outpost_prod():
    """S3 Outposts bucketAlias Ec2 Outpost Prod me-south-1"""
    params = EndpointParams(Region='me-south-1', Bucket='test-accessp-e0000075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://test-accessp-e0000075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3.ec2.s3-outposts.me-south-1.amazonaws.com'

def test_s3_outposts_bucketalias_real_outpost_bet():
    """S3 Outposts bucketAlias Real Outpost Beta"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kbeta0--op-s3', Endpoint='https://example.amazonaws.com', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kbeta0--op-s3.op-0b1d075431d83bebd.example.amazonaws.com'

def test_s3_outposts_bucketalias_ec2_outpost_beta():
    """S3 Outposts bucketAlias Ec2 Outpost Beta"""
    params = EndpointParams(Region='us-east-1', Bucket='161743052723-e00000136899934034jeahy1t8gpzpbwjj8kb7beta0--op-s3', Endpoint='https://example.amazonaws.com', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://161743052723-e00000136899934034jeahy1t8gpzpbwjj8kb7beta0--op-s3.ec2.example.amazonaws.com'

def test_s3_outposts_bucketalias___no_endpoint_se():
    """S3 Outposts bucketAlias - No endpoint set for beta"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-o0b1d075431d83bebde8xz5w8ijx1qzlbp3i3kbeta0--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Expected a endpoint to be specified but no endpoint was found')):
        resolve(params)

def test_s3_outposts_invalid_bucket_name():
    """S3 Outposts invalid bucket name"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-o0b1de75431d83bebd/8xz5w8ijx1qzlbp3i3kbeta0--op-s3', Endpoint='https://example.amazonaws.com', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Outposts Bucket alias - it must be a valid bucket name.')):
        resolve(params)

def test_s3_outposts_bucketalias_invalid_hardware():
    """S3 Outposts bucketAlias Invalid hardware type"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-h0000075431d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized hardware type: "Expected hardware type o or e but got h"')):
        resolve(params)

def test_s3_outposts_bucketalias_special_characte():
    """S3 Outposts bucketAlias Special character in Outpost Arn"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-o00000754%1d83bebde8xz5w8ijx1qzlbp3i3kuse10--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The outpost Id must only contain a-z, A-Z, 0-9 and `-`.')):
        resolve(params)

def test_s3_outposts_bucketalias___no_endpoint_se():
    """S3 Outposts bucketAlias - No endpoint set for beta"""
    params = EndpointParams(Region='us-east-1', Bucket='test-accessp-e0b1d075431d83bebde8xz5w8ijx1qzlbp3i3ebeta0--op-s3', UseFIPS=False, UseDualStack=False, Accelerate=False)
    with pytest.raises(EndpointError, match=re.escape('Expected a endpoint to be specified but no endpoint was found')):
        resolve(params)

def test_s3_snow_with_bucket():
    """S3 Snow with bucket"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='http://10.0.1.12:433', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'http://10.0.1.12:433/bucketName'

def test_s3_snow_without_bucket():
    """S3 Snow without bucket"""
    params = EndpointParams(Region='snow', Endpoint='https://10.0.1.12:433', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://10.0.1.12:433'

def test_s3_snow_no_port():
    """S3 Snow no port"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='http://10.0.1.12', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'http://10.0.1.12/bucketName'

def test_s3_snow_dns_endpoint():
    """S3 Snow dns endpoint"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='https://amazonaws.com', UseFIPS=False, UseDualStack=False, Accelerate=False)
    result = resolve(params)
    assert result.url == 'https://amazonaws.com/bucketName'

def test_data_plane_with_short_zone_name():
    """Data Plane with short zone name"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--abcd-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--abcd-ab1--x-s3.s3express-abcd-ab1.us-east-1.amazonaws.com'

def test_data_plane_with_short_zone_name_china_re():
    """Data Plane with short zone name china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='mybucket--abcd-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--abcd-ab1--x-s3.s3express-abcd-ab1.cn-north-1.amazonaws.com.cn'

def test_data_plane_with_short_zone_name_with_ap():
    """Data Plane with short zone name with AP"""
    params = EndpointParams(Region='us-east-1', Bucket='myaccesspoint--abcd-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--abcd-ab1--xa-s3.s3express-abcd-ab1.us-east-1.amazonaws.com'

def test_data_plane_with_short_zone_name_with_ap_():
    """Data Plane with short zone name with AP china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='myaccesspoint--abcd-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--abcd-ab1--xa-s3.s3express-abcd-ab1.cn-north-1.amazonaws.com.cn'

def test_data_plane_with_short_zone_names__13_cha():
    """Data Plane with short zone names (13 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_short_zone_names__13_cha():
    """Data Plane with short zone names (13 chars) with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_medium_zone_names__14_ch():
    """Data Plane with medium zone names (14 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_medium_zone_names__14_ch():
    """Data Plane with medium zone names (14 chars) with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone_names__20_char():
    """Data Plane with long zone names (20 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone_names__20_char():
    """Data Plane with long zone names (20 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_short_zone_fips():
    """Data Plane with short zone fips"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-ab1--x-s3.s3express-fips-test-ab1.us-east-1.amazonaws.com'

def test_data_plane_with_short_zone_fips_china_re():
    """Data Plane with short zone fips china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_data_plane_with_short_zone_fips_with_ap():
    """Data Plane with short zone fips with AP"""
    params = EndpointParams(Region='us-east-1', Bucket='myaccesspoint--test-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-ab1--xa-s3.s3express-fips-test-ab1.us-east-1.amazonaws.com'

def test_data_plane_with_short_zone_fips_with_ap_():
    """Data Plane with short zone fips with AP china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='myaccesspoint--test-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_data_plane_with_short_zone__13_chars__fi():
    """Data Plane with short zone (13 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-fips-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_short_zone__13_chars__fi():
    """Data Plane with short zone (13 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-fips-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_medium_zone__14_chars__f():
    """Data Plane with medium zone (14 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-fips-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_medium_zone__14_chars__f():
    """Data Plane with medium zone (14 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-fips-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone__20_chars__fip():
    """Data Plane with long zone (20 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-fips-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone__20_chars__fip():
    """Data Plane with long zone (20 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-fips-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_with_long_az():
    """Data Plane with long AZ"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-az1--x-s3.s3express-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_with_long_az_with_ap():
    """Data Plane with long AZ with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-az1--xa-s3.s3express-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_with_long_az_fips():
    """Data Plane with long AZ fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-az1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-az1--x-s3.s3express-fips-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_with_long_az_fips_with_ap():
    """Data Plane with long AZ fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-az1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-az1--xa-s3.s3express-fips-test1-az1.us-west-2.amazonaws.com'

def test_control_plane_with_short_az_bucket():
    """Control plane with short AZ bucket"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com/mybucket--test-ab1--x-s3'

def test_control_plane_with_short_az_bucket_china():
    """Control plane with short AZ bucket china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.cn-north-1.amazonaws.com.cn/mybucket--test-ab1--x-s3'

def test_control_plane_with_short_az_bucket_and_f():
    """Control plane with short AZ bucket and fips"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.us-east-1.amazonaws.com/mybucket--test-ab1--x-s3'

def test_control_plane_with_short_az_bucket_and_f():
    """Control plane with short AZ bucket and fips china region"""
    params = EndpointParams(Region='cn-north-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_control_plane_without_bucket():
    """Control plane without bucket"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com'

def test_control_plane_without_bucket_and_fips():
    """Control plane without bucket and fips"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.us-east-1.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az():
    """Data Plane sigv4 auth with short AZ"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-usw2-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az_with():
    """Data Plane sigv4 auth with short AZ with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-usw2-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_zone__1():
    """Data Plane sigv4 auth with short zone (13 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_zone__1():
    """Data Plane sigv4 auth with short zone (13 chars) with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az_fips():
    """Data Plane sigv4 auth with short AZ fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-fips-usw2-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az_fips():
    """Data Plane sigv4 auth with short AZ fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-fips-usw2-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_zone__1():
    """Data Plane sigv4 auth with short zone (13 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-fips-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_zone__1():
    """Data Plane sigv4 auth with short zone (13 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-fips-test-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_az():
    """Data Plane sigv4 auth with long AZ"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-az1--x-s3.s3express-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_az_with_():
    """Data Plane sigv4 auth with long AZ with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-az1--xa-s3.s3express-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_medium_zone_1():
    """Data Plane sigv4 auth with medium zone(14 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_medium_zone_1():
    """Data Plane sigv4 auth with medium zone(14 chars) with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone_20_():
    """Data Plane sigv4 auth with long zone(20 chars)"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone_20_():
    """Data Plane sigv4 auth with long zone(20 chars) with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_az_fips():
    """Data Plane sigv4 auth with long AZ fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-az1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-az1--x-s3.s3express-fips-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_az_fips_():
    """Data Plane sigv4 auth with long AZ fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-az1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-az1--xa-s3.s3express-fips-test1-az1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_medium_zone__():
    """Data Plane sigv4 auth with medium zone (14 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-fips-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_medium_zone__():
    """Data Plane sigv4 auth with medium zone (14 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-fips-test1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone__20():
    """Data Plane sigv4 auth with long zone (20 chars) fips"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-fips-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone__20():
    """Data Plane sigv4 auth with long zone (20 chars) fips with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-fips-test1-long1-zone-ab1.us-west-2.amazonaws.com'

def test_control_plane_host_override():
    """Control Plane host override"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=True, Endpoint='https://custom.com')
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.custom.com'

def test_control_plane_host_override_with_ap():
    """Control Plane host override with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=True, Endpoint='https://custom.com')
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.custom.com'

def test_control_plane_host_override_no_bucket():
    """Control Plane host override no bucket"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=True, Endpoint='https://custom.com')
    result = resolve(params)
    assert result.url == 'https://custom.com'

def test_data_plane_host_override_non_virtual_ses():
    """Data plane host override non virtual session auth"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://10.0.0.1')
    result = resolve(params)
    assert result.url == 'https://10.0.0.1/mybucket--usw2-az1--x-s3'

def test_data_plane_host_override_non_virtual_ses():
    """Data plane host override non virtual session auth with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://10.0.0.1')
    result = resolve(params)
    assert result.url == 'https://10.0.0.1/myaccesspoint--usw2-az1--xa-s3'

def test_control_plane_host_override_ip():
    """Control Plane host override ip"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=True, Endpoint='https://10.0.0.1')
    result = resolve(params)
    assert result.url == 'https://10.0.0.1/mybucket--usw2-az1--x-s3'

def test_control_plane_host_override_ip_with_ap():
    """Control Plane host override ip with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=True, Endpoint='https://10.0.0.1')
    result = resolve(params)
    assert result.url == 'https://10.0.0.1/myaccesspoint--usw2-az1--xa-s3'

def test_data_plane_host_override():
    """Data plane host override"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com')
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.custom.com'

def test_data_plane_host_override_with_ap():
    """Data plane host override with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com')
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.custom.com'

def test_bad_format_error():
    """bad format error"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--usaz1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized S3Express bucket name format.')):
        resolve(params)

def test_bad_ap_format_error():
    """bad AP format error"""
    params = EndpointParams(Region='us-east-1', Bucket='myaccesspoint--usaz1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized S3Express bucket name format.')):
        resolve(params)

def test_bad_format_error_no_session_auth():
    """bad format error no session auth"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--usaz1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized S3Express bucket name format.')):
        resolve(params)

def test_bad_ap_format_error_no_session_auth():
    """bad AP format error no session auth"""
    params = EndpointParams(Region='us-east-1', Bucket='myaccesspoint--usaz1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False, DisableS3ExpressSessionAuth=True)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized S3Express bucket name format.')):
        resolve(params)

def test_accelerate_error():
    """accelerate error"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=True, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express does not support S3 Accelerate.')):
        resolve(params)

def test_accelerate_error_with_ap():
    """accelerate error with AP"""
    params = EndpointParams(Region='us-east-1', Bucket='myaccesspoint--test-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=True, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express does not support S3 Accelerate.')):
        resolve(params)

def test_data_plane_bucket_format_error():
    """Data plane bucket format error"""
    params = EndpointParams(Region='us-east-1', Bucket='my.bucket--test-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_data_plane_ap_format_error():
    """Data plane AP format error"""
    params = EndpointParams(Region='us-east-1', Bucket='my.myaccesspoint--test-ab1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_host_override_data_plane_bucket_error_se():
    """host override data plane bucket error session auth"""
    params = EndpointParams(Region='us-west-2', Bucket='my.bucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com')
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_host_override_data_plane_ap_error_sessio():
    """host override data plane AP error session auth"""
    params = EndpointParams(Region='us-west-2', Bucket='my.myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com')
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_host_override_data_plane_bucket_error():
    """host override data plane bucket error"""
    params = EndpointParams(Region='us-west-2', Bucket='my.bucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com', DisableS3ExpressSessionAuth=True)
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_host_override_data_plane_ap_error():
    """host override data plane AP error"""
    params = EndpointParams(Region='us-west-2', Bucket='my.myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, Endpoint='https://custom.com', DisableS3ExpressSessionAuth=True)
    with pytest.raises(EndpointError, match=re.escape('S3Express bucket name is not a valid virtual hostable name.')):
        resolve(params)

def test_control_plane_without_bucket_and_dualsta():
    """Control plane without bucket and dualstack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.dualstack.us-east-1.amazonaws.com'

def test_control_plane_without_bucket__fips_and_d():
    """Control plane without bucket, fips and dualstack"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.dualstack.us-east-1.amazonaws.com'

def test_data_plane_with_bucket_containing_delimi():
    """Data Plane with bucket containing delimiters"""
    params = EndpointParams(Region='us-east-1', Bucket='my--s3--bucket--abcd-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://my--s3--bucket--abcd-ab1--x-s3.s3express-abcd-ab1.us-east-1.amazonaws.com'

def test_control_plane_with_with_bucket_containin():
    """Control plane with with bucket containing delimiters"""
    params = EndpointParams(Region='us-east-1', Bucket='my--s3--bucket--abcd-ab1--x-s3', UseFIPS=False, UseDualStack=False, Accelerate=False, UseS3ExpressControlEndpoint=True, DisableS3ExpressSessionAuth=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com/my--s3--bucket--abcd-ab1--x-s3'

def test_data_plane_with_short_az_and_dualstack():
    """Data Plane with short AZ and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_short_az_and_fips_with_d():
    """Data Plane with short AZ and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-fips-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az_and_():
    """Data Plane sigv4 auth with short AZ and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_short_az_and_():
    """Data Plane sigv4 auth with short AZ and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az1--x-s3.s3express-fips-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone_and_dualstack():
    """Data Plane with zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az12--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az12--x-s3.s3express-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone_and_fips_with_duals():
    """Data Plane with zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az12--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az12--x-s3.s3express-fips-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_zone_and_dual():
    """Data Plane sigv4 auth with zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az12--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az12--x-s3.s3express-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_9_char_zone_a():
    """Data Plane sigv4 auth with 9-char zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--usw2-az12--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--usw2-az12--x-s3.s3express-fips-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_13_char_zone_and_dualsta():
    """Data Plane with 13-char zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_13_char_zone_and_fips_wi():
    """Data Plane with 13-char zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-fips-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_13_char_zone_():
    """Data Plane sigv4 auth with 13-char zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_13_char_zone_():
    """Data Plane sigv4 auth with 13-char zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test-zone-ab1--x-s3.s3express-fips-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_14_char_zone_and_dualsta():
    """Data Plane with 14-char zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_14_char_zone_and_fips_wi():
    """Data Plane with 14-char zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-fips-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_14_char_zone_():
    """Data Plane sigv4 auth with 14-char zone and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_14_char_zone_():
    """Data Plane sigv4 auth with 14-char zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-zone-ab1--x-s3.s3express-fips-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone__20_cha__and_d():
    """Data Plane with long zone (20 cha) and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_long_zone__20_char__and_():
    """Data Plane with long zone (20 char) and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-fips-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone__20():
    """Data Plane sigv4 auth with long zone (20 char) and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_long_zone__20():
    """Data Plane sigv4 auth with long zone (20 char) and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='mybucket--test1-long1-zone-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://mybucket--test1-long1-zone-ab1--x-s3.s3express-fips-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_control_plane_and_fips_with_dualstack():
    """Control plane and FIPS with dualstack"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.dualstack.us-east-1.amazonaws.com/mybucket--test-ab1--x-s3'

def test_data_plane_with_zone_and_dualstack_and_a():
    """Data plane with zone and dualstack and AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone_and_fips_with_duals():
    """Data plane with zone and FIPS with dualstack and AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-fips-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with_zone_and_dual():
    """Data Plane sigv4 auth with zone and dualstack and AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_ap_sigv4_auth_with_zone_and_f():
    """Data Plane AP sigv4 auth with zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az1--xa-s3.s3express-fips-usw2-az1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone__9_char__and_ap_wit():
    """Data Plane with zone (9 char) and AP with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az12--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az12--xa-s3.s3express-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone__9_char__and_fips_w():
    """Data Plane with zone (9 char) and FIPS with AP and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az12--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az12--xa-s3.s3express-fips-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with__9_char__zone():
    """Data Plane sigv4 auth with (9 char) zone and dualstack with AP"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az12--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az12--xa-s3.s3express-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_access_point_sigv4_auth_with__9_char__zo():
    """Access Point sigv4 auth with (9 char) zone and FIPS with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--usw2-az12--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--usw2-az12--xa-s3.s3express-fips-usw2-az12.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone__13_char__and_ap_wi():
    """Data Plane with zone (13 char) and AP with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with_zone__13_char__and_ap_wi():
    """Data Plane with zone (13 char) and AP with FIPS and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-fips-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with__13_char__zon():
    """Data Plane sigv4 auth with (13 char) zone with AP and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with__13_char__zon():
    """Data Plane sigv4 auth with (13 char) zone with AP and FIPS and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test-zone-ab1--xa-s3.s3express-fips-test-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with__14_char__zone_and_ap_wi():
    """Data Plane with (14 char) zone and AP with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with__14_char__zone_and_ap_wi():
    """Data Plane with (14 char) zone and AP with FIPS and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-fips-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_sigv4_auth_with__14_char__zon():
    """Data Plane sigv4 auth with (14 char) zone and AP with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with__14_char__zone_and_ap_wi():
    """Data Plane with (14 char) zone and AP with FIPS and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-zone-ab1--xa-s3.s3express-fips-test1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with__20_char__zone_and_ap_wi():
    """Data Plane with (20 char) zone and AP with dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_with__20_char__zone_and_ap_wi():
    """Data Plane with (20 char) zone and AP with FIPS and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=False)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-fips-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_ap_with_sigv4_and_dualstack():
    """Data plane AP with sigv4 and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_data_plane_ap_sigv4_with_fips_and_dualst():
    """Data plane AP sigv4 with fips and dualstack"""
    params = EndpointParams(Region='us-west-2', Bucket='myaccesspoint--test1-long1-zone-ab1--xa-s3', UseFIPS=True, UseDualStack=True, Accelerate=False, DisableS3ExpressSessionAuth=True)
    result = resolve(params)
    assert result.url == 'https://myaccesspoint--test1-long1-zone-ab1--xa-s3.s3express-fips-test1-long1-zone-ab1.dualstack.us-west-2.amazonaws.com'

def test_control_plane_with_dualstack_and_bucket():
    """Control plane with dualstack and bucket"""
    params = EndpointParams(Region='us-east-1', Bucket='mybucket--test-ab1--x-s3', UseFIPS=False, UseDualStack=True, Accelerate=False, UseS3ExpressControlEndpoint=True)
    result = resolve(params)
    assert result.url == 'https://s3express-control.dualstack.us-east-1.amazonaws.com/mybucket--test-ab1--x-s3'