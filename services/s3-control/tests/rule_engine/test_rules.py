import pytest
from aws_sdk_s3_control._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_s3_control._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_vanilla_outposts_without_arn_region___ac():
    """Vanilla outposts without ARN region + access point ARN@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_vanilla_outposts_with_arn_region___acces():
    """Vanilla outposts with ARN region + access point ARN@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_accept_an_access_point_arn_us_west_2():
    """accept an access point ARN@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_vanilla_outposts_china_cn_north_1():
    """vanilla outposts china@cn-north-1"""
    params = EndpointParams(AccessPointName='arn:aws-cn:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.cn-north-1.amazonaws.com.cn'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_region_us_west_2():
    """gov region@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_cloud_with_fips_us_west_2():
    """gov cloud with fips@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_govcloud_with_fips___arn_region_us_gov_w():
    """govcloud with fips + arn region@us-gov-west-1"""
    params = EndpointParams(AccessPointName='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_region_cn_north_1():
    """gov region@cn-north-1"""
    params = EndpointParams(AccessPointName='arn:aws-cn:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.cn-north-1.amazonaws.com.cn'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_cloud_with_fips_cn_north_1():
    """gov cloud with fips@cn-north-1"""
    params = EndpointParams(AccessPointName='arn:aws-cn:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_govcloud_with_fips___arn_region_us_gov_w():
    """govcloud with fips + arn region@us-gov-west-1"""
    params = EndpointParams(AccessPointName='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_region_af_south_1():
    """gov region@af-south-1"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:af-south-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='af-south-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.af-south-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_gov_cloud_with_fips_af_south_1():
    """gov cloud with fips@af-south-1"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:af-south-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='af-south-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.af-south-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_govcloud_with_fips___arn_region_us_gov_w():
    """govcloud with fips + arn region@us-gov-west-1"""
    params = EndpointParams(AccessPointName='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_createbucket___outpostid___outposts_endp():
    """CreateBucket + OutpostId = outposts endpoint@us-east-2"""
    params = EndpointParams(Bucket='blah', OutpostId='123', Region='us-east-2', RequiresAccountId=False, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-2.amazonaws.com'

def test_createbucket___outpostid_with_fips___out():
    """CreateBucket + OutpostId with fips = outposts endpoint@us-east-2"""
    params = EndpointParams(Bucket='blah', OutpostId='123', Region='us-east-2', RequiresAccountId=False, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.amazonaws.com'

def test_createbucket_without_outpostid___regular():
    """CreateBucket without OutpostId = regular endpoint@us-east-2"""
    params = EndpointParams(Bucket='blah', Region='us-east-2', RequiresAccountId=False, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-control.us-east-2.amazonaws.com'

def test_listregionalbuckets___outpostid___outpos():
    """ListRegionalBuckets + OutpostId = outposts endpoint@us-east-2"""
    params = EndpointParams(AccountId='123456789012', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-2.amazonaws.com'

def test_listregionalbuckets_without_outpostid___():
    """ListRegionalBuckets without OutpostId = regular endpoint@us-east-2"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://123456789012.s3-control.us-east-2.amazonaws.com'

def test_listregionalbucket___outpostid_with_fips():
    """ListRegionalBucket + OutpostId with fips = outposts endpoint@us-east-2"""
    params = EndpointParams(AccountId='123456789012', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.amazonaws.com'

def test_outpost_access_points_support_dualstack_():
    """outpost access points support dualstack@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.api.aws'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_outpost_access_points_support_dualstack_():
    """outpost access points support dualstack@af-south-1"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:af-south-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='af-south-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.af-south-1.api.aws'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_outpost_access_points_support_fips___dua():
    """outpost access points support fips + dualstack@af-south-1"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:af-south-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='af-south-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.af-south-1.api.aws'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_invalid_arn__must_be_include_outpost_id_():
    """invalid ARN: must be include outpost ID@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The Outpost Id was not set')):
        resolve(params)

def test_invalid_arn__must_specify_access_point_u():
    """invalid ARN: must specify access point@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a 4-component resource')):
        resolve(params)

def test_invalid_arn_us_west_2():
    """invalid ARN@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:myaccesspoint', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a 4-component resource')):
        resolve(params)

def test_when_set__accountid_drives_ap_constructi():
    """when set, AccountId drives AP construction@us-west-2"""
    params = EndpointParams(AccessPointName='myaccesspoint', AccountId='myid-1234', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://myid-1234.s3-control.us-west-2.amazonaws.com'

def test_account_id_set_inline_and_in_arn_but_the():
    """Account ID set inline and in ARN but they both match@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseArnRegion=False, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_account_id_set_inline_and_in_arn_and_the():
    """Account ID set inline and in ARN and they do not match@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='999999999999', Region='us-west-2', RequiresAccountId=True, UseArnRegion=False, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: the accountId specified in the ARN (`123456789012`) does not match the parameter (`999999999999`)')):
        resolve(params)

def test_get_access_point_prefixed_with_account_i():
    """get access point prefixed with account id using endpoint url@us-west-2"""
    params = EndpointParams(AccessPointName='apname', AccountId='123456789012', Endpoint='https://control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://123456789012.control.vpce-1a2b3c4d-5e6f.s3.us-west-2.vpce.amazonaws.com'

def test_endpoint_url_with_s3_outposts_us_west_2():
    """endpoint url with s3-outposts@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Endpoint='https://beta.example.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_access_point_name_with_a_bucket_arn_us_w():
    """access point name with a bucket arn@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Endpoint='beta.example.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Expected an outpost type `accesspoint`, found `bucket`')):
        resolve(params)

def test_bucket_arn_with_access_point_name_us_wes():
    """bucket arn with access point name@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', Endpoint='beta.example.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected an outpost type `bucket`, found `accesspoint`')):
        resolve(params)

def test_create_bucket_with_outposts_us_west_2():
    """create bucket with outposts@us-west-2"""
    params = EndpointParams(Bucket='bucketname', Endpoint='https://beta.example.com', OutpostId='op-123', Region='us-west-2', RequiresAccountId=False, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'

def test_get_bucket_with_endpoint_url_us_west_2():
    """get bucket with endpoint_url@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Endpoint='https://beta.example.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_listregionalbucket___outpostid_endpoint_():
    """ListRegionalBucket + OutpostId endpoint url@us-east-2"""
    params = EndpointParams(AccountId='123456789012', Endpoint='https://beta.example.com', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'

def test_listregionalbucket___outpostid___fips___():
    """ListRegionalBucket + OutpostId + fips + endpoint url@us-east-2"""
    params = EndpointParams(AccountId='123456789012', Endpoint='https://beta.example.com', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'

def test_listregionalbucket___outpostid___fips___():
    """ListRegionalBucket + OutpostId + fips + dualstack@us-east-2"""
    params = EndpointParams(AccountId='123456789012', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.api.aws'

def test_createbucket___outpostid_endpoint_url_us():
    """CreateBucket + OutpostId endpoint url@us-east-2"""
    params = EndpointParams(Bucket='blah', Endpoint='https://beta.example.com', OutpostId='123', Region='us-east-2', RequiresAccountId=False, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'

def test_dualstack_cannot_be_used_with_outposts_w():
    """dualstack cannot be used with outposts when an endpoint URL is set@us-west-2."""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', Endpoint='https://s3-outposts.us-west-2.api.aws', Region='us-west-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_vanilla_bucket_arn_requires_account_id_u():
    """vanilla bucket arn requires account id@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_with_usearnregion___true__arn():
    """bucket arn with UseArnRegion = true (arn region supercedes client configured region)@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition__non_fips__u():
    """bucket ARN in gov partition (non-fips)@us-gov-east-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition_with_fips_us():
    """bucket ARN in gov partition with FIPS@us-gov-west-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-west-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-west-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_aws_partition_with_fips_us():
    """bucket ARN in aws partition with FIPS@us-east-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_aws_partition_with_fips___():
    """bucket ARN in aws partition with fips + dualstack@us-east-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-east-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.api.aws'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_vanilla_bucket_arn_requires_account_id_c():
    """vanilla bucket arn requires account id@cn-north-1"""
    params = EndpointParams(Bucket='arn:aws-cn:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.cn-north-1.amazonaws.com.cn'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_with_usearnregion___true__arn():
    """bucket arn with UseArnRegion = true (arn region supercedes client configured region)@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition__non_fips__u():
    """bucket ARN in gov partition (non-fips)@us-gov-east-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition_with_fips_us():
    """bucket ARN in gov partition with FIPS@us-gov-west-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-west-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-west-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_aws_partition_with_fips_us():
    """bucket ARN in aws partition with FIPS@us-east-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_outposts_support_dualstack__us_west_2():
    """Outposts support dualstack @us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.api.aws'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_vanilla_bucket_arn_requires_account_id_a():
    """vanilla bucket arn requires account id@af-south-1"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:af-south-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='af-south-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.af-south-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_with_usearnregion___true__arn():
    """bucket arn with UseArnRegion = true (arn region supercedes client configured region)@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition__non_fips__u():
    """bucket ARN in gov partition (non-fips)@us-gov-east-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-gov-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_gov_partition_with_fips_us():
    """bucket ARN in gov partition with FIPS@us-gov-west-1"""
    params = EndpointParams(Bucket='arn:aws-us-gov:s3-outposts:us-gov-west-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-gov-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-gov-west-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_in_aws_partition_with_fips_us():
    """bucket ARN in aws partition with FIPS@us-east-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-outposts-fips.us-east-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_invalid_arn__missing_outpost_id_and_buck():
    """Invalid ARN: missing outpost id and bucket@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: The Outpost Id was not set')):
        resolve(params)

def test_invalid_arn__missing_bucket_us_west_2():
    """Invalid ARN: missing bucket@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a 4-component resource')):
        resolve(params)

def test_invalid_arn__missing_outpost_and_bucket_():
    """Invalid ARN: missing outpost and bucket ids@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:bucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: Expected a 4-component resource')):
        resolve(params)

def test_invalid_arn__missing_bucket_id_us_west_2():
    """Invalid ARN: missing bucket id@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: expected a bucket name')):
        resolve(params)

def test_account_id_inserted_into_hostname_us_wes():
    """account id inserted into hostname@us-west-2"""
    params = EndpointParams(AccountId='1234567890', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://1234567890.s3-control.us-west-2.amazonaws.com'

def test_account_id_prefix_with_dualstack_us_east():
    """account id prefix with dualstack@us-east-1"""
    params = EndpointParams(AccountId='1234567890', Region='us-east-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://1234567890.s3-control.dualstack.us-east-1.amazonaws.com'

def test_account_id_prefix_with_fips_us_east_1():
    """account id prefix with fips@us-east-1"""
    params = EndpointParams(AccountId='1234567890', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://1234567890.s3-control-fips.us-east-1.amazonaws.com'

def test_custom_account_id_prefix_with_fips_us_ea():
    """custom account id prefix with fips@us-east-1"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.s3-control-fips.us-east-1.amazonaws.com'

def test_standard_url___us_east_1():
    """standard url @ us-east-1"""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://s3-control.us-east-1.amazonaws.com'

def test_fips_url___us_east_1():
    """fips url @ us-east-1"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-control-fips.us-east-1.amazonaws.com'

def test_dualstack_url___us_east_1():
    """dualstack url @ us-east-1"""
    params = EndpointParams(Region='us-east-1', UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://s3-control.dualstack.us-east-1.amazonaws.com'

def test_fips_dualstack_url___us_east_1():
    """fips,dualstack url @ us-east-1"""
    params = EndpointParams(Region='us-east-1', UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3-control-fips.dualstack.us-east-1.amazonaws.com'

def test_standard_url___cn_north_1():
    """standard url @ cn-north-1"""
    params = EndpointParams(Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://s3-control.cn-north-1.amazonaws.com.cn'

def test_fips___cn_north_1():
    """fips @ cn-north-1"""
    params = EndpointParams(Region='cn-north-1', UseDualStack=True, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_custom_account_id_prefix__us_east_1():
    """custom account id prefix @us-east-1"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://123456789012.s3-control.us-east-1.amazonaws.com'

def test_invalid_account_id_prefix__us_east_1():
    """invalid account id prefix @us-east-1"""
    params = EndpointParams(AccountId='/?invalid&not-host*label', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('AccountId must only contain a-z, A-Z, 0-9 and `-`.')):
        resolve(params)

def test_custom_account_id_prefix_with_fips_us_ea():
    """custom account id prefix with fips@us-east-1"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.s3-control-fips.us-east-1.amazonaws.com'

def test_custom_account_id_prefix_with_dualstack_():
    """custom account id prefix with dualstack,fips@us-east-1"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.s3-control-fips.dualstack.us-east-1.amazonaws.com'

def test_custom_account_id_with_custom_endpoint():
    """custom account id with custom endpoint"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://123456789012.example.com'

def test_requiresaccountid_with_accountid_unset():
    """RequiresAccountId with AccountId unset"""
    params = EndpointParams(Region='us-east-1', RequiresAccountId=True)
    with pytest.raises(EndpointError, match=re.escape('AccountId is required but not set')):
        resolve(params)

def test_requiresaccountid_with_accountid_unset_a():
    """RequiresAccountId with AccountId unset and custom endpoint"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://beta.example.com', RequiresAccountId=True)
    with pytest.raises(EndpointError, match=re.escape('AccountId is required but not set')):
        resolve(params)

def test_requiresaccountid_with_invalid_accountid():
    """RequiresAccountId with invalid AccountId and custom endpoint"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://beta.example.com', AccountId='/?invalid&not-host*label', RequiresAccountId=True)
    with pytest.raises(EndpointError, match=re.escape('AccountId must only contain a-z, A-Z, 0-9 and `-`.')):
        resolve(params)

def test_account_id_with_custom_endpoint__fips():
    """account id with custom endpoint, fips"""
    params = EndpointParams(AccountId='123456789012', Region='us-east-1', RequiresAccountId=True, Endpoint='https://example.com', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.example.com'

def test_custom_endpoint__fips():
    """custom endpoint, fips"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_custom_endpoint__fips():
    """custom endpoint, fips"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_custom_endpoint__dualstack():
    """custom endpoint, DualStack"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_region_not_set():
    """region not set"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Region must be set')):
        resolve(params)

def test_invalid_partition():
    """invalid partition"""
    params = EndpointParams(Region='invalid-region 42')
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_listregionalbuckets___outpostid_without_():
    """ListRegionalBuckets + OutpostId without accountId set."""
    params = EndpointParams(OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('AccountId is required but not set')):
        resolve(params)

def test_listregionalbuckets___outpostid_with_inv():
    """ListRegionalBuckets + OutpostId with invalid accountId set."""
    params = EndpointParams(AccountId='/?invalid&not-host*label', OutpostId='op-123', Region='us-east-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('AccountId must only contain a-z, A-Z, 0-9 and `-`.')):
        resolve(params)

def test_accesspoint_set_but_missing_accountid():
    """accesspoint set but missing accountId"""
    params = EndpointParams(AccessPointName='myaccesspoint', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('AccountId is required but not set')):
        resolve(params)

def test_outpost_accesspoint_arn_with_missing_acc():
    """outpost accesspoint ARN with missing accountId"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2::outpost:op-01234567890123456:outpost:op1', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: missing account ID')):
        resolve(params)

def test_bucket_arn_with_missing_accountid():
    """bucket ARN with missing accountId"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2::outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: missing account ID')):
        resolve(params)

def test_endpoint_url_with_accesspoint__non_arn_():
    """endpoint url with accesspoint (non-arn)"""
    params = EndpointParams(AccessPointName='apname', Endpoint='https://beta.example.com', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://123456789012.beta.example.com'

def test_access_point_name_with_an_accesspoint_ar():
    """access point name with an accesspoint arn@us-west-2"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', Endpoint='https://beta.example.com', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://beta.example.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_dualstack___custom_endpoint_is_not_suppo():
    """DualStack + Custom endpoint is not supported(non-arn)"""
    params = EndpointParams(AccessPointName='apname', Endpoint='https://beta.example.com', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_get_bucket_with_custom_endpoint_and_dual():
    """get bucket with custom endpoint and dualstack is not supported@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Endpoint='https://s3-outposts.us-west-2.api.aws', Region='us-west-2', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_listregionalbuckets___outpostid_with_fip():
    """ListRegionalBuckets + OutpostId with fips in CN."""
    params = EndpointParams(AccountId='012345678912', OutpostId='op-123', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_listregionalbuckets___invalid_outpostid_():
    """ListRegionalBuckets + invalid OutpostId."""
    params = EndpointParams(AccountId='012345678912', OutpostId='?outpost/invalid+', Region='us-west-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('OutpostId must only contain a-z, A-Z, 0-9 and `-`.')):
        resolve(params)

def test_bucket_arn_with_mismatched_accountid():
    """bucket ARN with mismatched accountId"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:999999:outpost:op-01234567890123456:bucket:mybucket', AccountId='012345678912', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid ARN: the accountId specified in the ARN (`999999`) does not match the parameter (`012345678912`)')):
        resolve(params)

def test_outpostid_with_invalid_region():
    """OutpostId with invalid region"""
    params = EndpointParams(OutpostId='op-123', Region='invalid-region 42', AccountId='0123456', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid region: region was not a valid DNS name.')):
        resolve(params)

def test_outpostid_with_requireaccountid_unset():
    """OutpostId with RequireAccountId unset"""
    params = EndpointParams(OutpostId='op-123', Region='us-west-2', UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'

def test_outpost_accesspoint_arn_with_arn_region_():
    """Outpost Accesspoint ARN with arn region and client region mismatch with UseArnRegion=false"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseArnRegion=False, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_outpost_bucket_arn_with_arn_region_and_c():
    """Outpost Bucket ARN with arn region and client region mismatch with UseArnRegion=false"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Endpoint='https://beta.example.com', Region='us-west-2', RequiresAccountId=True, UseArnRegion=False, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `us-east-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_accesspoint_arn_with_region_mismatch_and():
    """Accesspoint ARN with region mismatch and UseArnRegion unset"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_bucket_arn_with_region_mismatch_and_usea():
    """Bucket ARN with region mismatch and UseArnRegion unset"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-east-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-east-1.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_outpost_bucket_arn_with_partition_mismat():
    """Outpost Bucket ARN with partition mismatch with UseArnRegion=true"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseArnRegion=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but ARN has `aws-cn`')):
        resolve(params)

def test_accesspoint_arn_with_partition_mismatch_():
    """Accesspoint ARN with partition mismatch and UseArnRegion=true"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', AccountId='123456789012', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseArnRegion=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Client was configured for partition `aws` but ARN has `aws-cn`')):
        resolve(params)

def test_accesspoint_arn_with_region_mismatch__us():
    """Accesspoint ARN with region mismatch, UseArnRegion=false and custom endpoint"""
    params = EndpointParams(AccessPointName='arn:aws:s3-outposts:cn-north-1:123456789012:outpost:op-01234567890123456:accesspoint:myaccesspoint', Region='us-west-2', Endpoint='https://example.com', RequiresAccountId=True, UseDualStack=False, UseArnRegion=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid configuration: region from ARN `cn-north-1` does not match client region `us-west-2` and UseArnRegion is `false`')):
        resolve(params)

def test_outpost_bucket_arn_us_west_2():
    """outpost bucket arn@us-west-2"""
    params = EndpointParams(Bucket='arn:aws:s3-outposts:us-west-2:123456789012:outpost:op-01234567890123456:bucket:mybucket', Region='us-west-2', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3-outposts.us-west-2.amazonaws.com'
    assert result.headers.get('x-amz-account-id') == ['123456789012']
    assert result.headers.get('x-amz-outpost-id') == ['op-01234567890123456']

def test_s3_snow_control_with_bucket():
    """S3 Snow Control with bucket"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='https://10.0.1.12:433', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://10.0.1.12:433'

def test_s3_snow_control_without_bucket():
    """S3 Snow Control without bucket"""
    params = EndpointParams(Region='snow', Endpoint='https://10.0.1.12:433', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://10.0.1.12:433'

def test_s3_snow_control_with_bucket_and_without_():
    """S3 Snow Control with bucket and without port"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='https://10.0.1.12', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://10.0.1.12'

def test_s3_snow_control_with_bucket_and_with_dns():
    """S3 Snow Control with bucket and with DNS"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='http://s3snow.com', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://s3snow.com'

def test_s3_snow_control_with_fips_enabled():
    """S3 Snow Control with FIPS enabled"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='https://10.0.1.12:433', UseFIPS=True, UseDualStack=False)
    with pytest.raises(EndpointError, match=re.escape('S3 Snow does not support FIPS')):
        resolve(params)

def test_s3_snow_control_with_dualstack_enabled():
    """S3 Snow Control with Dualstack enabled"""
    params = EndpointParams(Region='snow', Bucket='bucketName', Endpoint='https://10.0.1.12:433', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('S3 Snow does not support DualStack')):
        resolve(params)

def test_tagging_on_express_bucket_routed_to_s3ex():
    """Tagging on express bucket routed to s3express-control"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:bucket/crachlintest--use1-az4--x-s3', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com'

def test_tagging_on_express_ap_routed_to_s3expres():
    """Tagging on express ap routed to s3express-control"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:accesspoint/crachlintest--use1-az4--xa-s3', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com'

def test_tagging_on_express_bucket_routed_to_s3ex():
    """Tagging on express bucket routed to s3express-control FIPS when FIPS enabled"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:bucket/crachlintest--use1-az4--x-s3', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.us-east-1.amazonaws.com'

def test_tagging_on_express_bucket_cn_routed_to_s():
    """Tagging on express bucket cn routed to s3express-control china endpoint"""
    params = EndpointParams(ResourceArn='arn:aws-cn:s3express:cn-north-1:871317572157:bucket/crachlintest--use1-az4--x-s3', AccountId='871317572157', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.cn-north-1.amazonaws.com.cn'

def test_tagging_on_express_bucket_cn_routed_to_s():
    """Tagging on express bucket cn routed to s3express-control china endpoint with FIPS"""
    params = EndpointParams(ResourceArn='arn:aws-cn:s3express:cn-north-1:871317572157:bucket/crachlintest--use1-az4--x-s3', AccountId='871317572157', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_tagging_on_express_bucket_with_custom_en():
    """Tagging on express bucket with custom endpoint routed to custom endpoint"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:bucket/crachlintest--use1-az4--x-s3', Endpoint='https://my-endpoint.express-control.s3.aws.dev', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://my-endpoint.express-control.s3.aws.dev'

def test_tagging_on_express_access_point_with_cus():
    """Tagging on express access point with custom endpoint routed to custom endpoint"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:accesspoint/crachlintest--use1-az4--xa-s3', Endpoint='https://my-endpoint.express-control.s3.aws.dev', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://my-endpoint.express-control.s3.aws.dev'

def test_tagging_on_express_bucket_with_dualstack():
    """Tagging on express bucket with dualstack and custom endpoint fails"""
    params = EndpointParams(ResourceArn='arn:aws:s3express:us-east-1:871317572157:bucket/crachlintest--use1-az4--x-s3', Endpoint='https://my-endpoint.express-control.s3.aws.dev', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control"""
    params = EndpointParams(AccountId='871317572157', AccessPointName='myaccesspoint--abcd-ab1--xa-s3', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control for List"""
    params = EndpointParams(AccountId='871317572157', Region='us-east-1', UseS3ExpressControlEndpoint=True, RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.us-east-1.amazonaws.com'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control for FIPS"""
    params = EndpointParams(AccountId='871317572157', AccessPointName='myaccesspoint--abcd-ab1--xa-s3', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.us-east-1.amazonaws.com'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control for FIPS for List"""
    params = EndpointParams(AccountId='871317572157', Region='us-east-1', UseS3ExpressControlEndpoint=True, RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://s3express-control-fips.us-east-1.amazonaws.com'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control for china region"""
    params = EndpointParams(AccessPointName='myaccesspoint--abcd-ab1--xa-s3', AccountId='871317572157', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.cn-north-1.amazonaws.com.cn'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to s3express-control for china region for List"""
    params = EndpointParams(AccountId='871317572157', Region='cn-north-1', UseS3ExpressControlEndpoint=True, RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://s3express-control.cn-north-1.amazonaws.com.cn'

def test_error_when_access_point_apis_on_express_():
    """Error when Access Point APIs on express bucket routed to s3express-control for china and FIPS"""
    params = EndpointParams(AccountId='871317572157', Region='cn-north-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Partition does not support FIPS')):
        resolve(params)

def test_error_access_point_apis_on_express_bucke():
    """Error Access Point APIs on express bucket routed to s3express-control invalid zone"""
    params = EndpointParams(AccessPointName='myaccesspoint-garbage-zone--xa-s3', AccountId='871317572157', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Unrecognized S3Express Access Point name format.')):
        resolve(params)

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to custom endpoint if provided"""
    params = EndpointParams(AccountId='871317572157', AccessPointName='myaccesspoint--abcd-ab1--xa-s3', Endpoint='https://my-endpoint.express-control.s3.aws.dev', Region='us-east-1', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://my-endpoint.express-control.s3.aws.dev'

def test_access_point_apis_on_express_bucket_rout():
    """Access Point APIs on express bucket routed to custom endpoint if provided for List"""
    params = EndpointParams(AccountId='871317572157', Region='us-east-1', UseS3ExpressControlEndpoint=True, Endpoint='https://my-endpoint.express-control.s3.aws.dev', RequiresAccountId=True, UseDualStack=False, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://my-endpoint.express-control.s3.aws.dev'

def test_error_on_access_point_apis_on_express_bu():
    """Error on Access Point APIs on express bucket for dual stack"""
    params = EndpointParams(AccountId='871317572157', AccessPointName='myaccesspoint--abcd-ab1--xa-s3', Region='us-east-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express does not support Dual-stack.')):
        resolve(params)

def test_error_access_point_apis_on_express_bucke():
    """Error Access Point APIs on express bucket for dual stack for List"""
    params = EndpointParams(AccountId='871317572157', Region='us-east-1', UseS3ExpressControlEndpoint=True, RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('S3Express does not support Dual-stack.')):
        resolve(params)

def test_error_on_access_point_apis_on_express_bu():
    """Error on Access Point APIs on express bucket for custom endpoint and dual stack"""
    params = EndpointParams(AccountId='871317572157', AccessPointName='myaccesspoint--abcd-ab1--xa-s3', Endpoint='https://my-endpoint.express-control.s3.aws.dev', Region='us-east-1', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)

def test_error_access_point_apis_on_express_bucke():
    """Error Access Point APIs on express bucket for custom endpoint and dual stack for List"""
    params = EndpointParams(AccountId='871317572157', Region='us-east-1', UseS3ExpressControlEndpoint=True, Endpoint='https://my-endpoint.express-control.s3.aws.dev', RequiresAccountId=True, UseDualStack=True, UseFIPS=False)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: DualStack and custom endpoint are not supported')):
        resolve(params)