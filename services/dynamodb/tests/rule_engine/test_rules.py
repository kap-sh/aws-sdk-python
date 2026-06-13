import pytest
from aws_sdk_dynamodb._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_dynamodb._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_1_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.af-south-1.amazonaws.com'

def test_2_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-east-1.amazonaws.com'

def test_3_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-1.amazonaws.com'

def test_4_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-2.amazonaws.com'

def test_5_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-northeast-3.amazonaws.com'

def test_6_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-south-1.amazonaws.com'

def test_7_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-1.amazonaws.com'

def test_8_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-2.amazonaws.com'

def test_9_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ap-southeast-3.amazonaws.com'

def test_10_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.ca-central-1.amazonaws.com'

def test_11_for_region_ca_central_1_with_fips_enable():
    """For region ca-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.ca-central-1.amazonaws.com'

def test_12_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-central-1.amazonaws.com'

def test_13_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-north-1.amazonaws.com'

def test_14_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-south-1.amazonaws.com'

def test_15_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-1.amazonaws.com'

def test_16_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-2.amazonaws.com'

def test_17_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.eu-west-3.amazonaws.com'

def test_18_for_region_local_with_fips_disabled_and_():
    """For region local with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='local', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_19_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.me-south-1.amazonaws.com'

def test_20_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.sa-east-1.amazonaws.com'

def test_21_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_22_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_23_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-2.amazonaws.com'

def test_24_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-2.amazonaws.com'

def test_25_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-west-1.amazonaws.com'

def test_26_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-west-1.amazonaws.com'

def test_27_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-west-2.amazonaws.com'

def test_28_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-west-2.amazonaws.com'

def test_29_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_30_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test_31_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_32_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-northwest-1.amazonaws.com.cn'

def test_33_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_34_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_35_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_36_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_37_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_38_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-west-1.amazonaws.com'

def test_39_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-west-1.amazonaws.com'

def test_40_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test_41_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test_42_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_43_for_region_us_iso_west_1_with_fips_disab():
    """For region us-iso-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-west-1.c2s.ic.gov'

def test_44_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_45_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-isob-east-1.sc2s.sgov.gov'

def test_46_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-isob-east-1.sc2s.sgov.gov'

def test_47_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_48_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_49_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_50_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_51_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test_52__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_53__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_54__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_55__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_56__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_57__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_58__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_59__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_60__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_61__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_62__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_63__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_64__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_65__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_66__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_67__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_68__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_69__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_70__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_71__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_72__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_73__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_74__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_75__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_76__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_77__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_78__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_79__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_80__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_81__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_82__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_83__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_84__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_85__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_86__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_87__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_88__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_89__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_90__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_91__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_92__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_93__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_94__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_95__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_96__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_97__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_98__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_99__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=disabled, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='disabled', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_100__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_101__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_102__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_103__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_104__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_105__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_106__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_107__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_108__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_109__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_110__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_111__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_112__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_113__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_114__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_115__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_116__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_117__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_118__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_119__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_120__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_121__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_122__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_123__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=required, Region=us-east-1, Endpoint=https://example.com}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='required', Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_124__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_125__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_126__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_127__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_128__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_129__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_130__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_131__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_132__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_133__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_134__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_135__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_136__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_137__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_138__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_139__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_140__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_141__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_142__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_143__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_144__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_145__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_146__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_147__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_148__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_149__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_150__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_151__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_152__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_153__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_154__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_155__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_156__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_157__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_158__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_159__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_160__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_161__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_162__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_163__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_164__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_165__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_166__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_167__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_168__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_169__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_170__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_171__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=disabled, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='disabled', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_172__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_173__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_174__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_175__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_176__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_177__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_178__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_179__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_180__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_181__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_182__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_183__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_184__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_185__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_186__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_187__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_188__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_189__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_190__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_191__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and local endpoint are not supported')):
        resolve(params)

def test_192__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and local endpoint are not supported')):
        resolve(params)

def test_193__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_194__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_195__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=required, Region=local}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='required', Region='local')
    result = resolve(params)
    assert result.url == 'http://localhost:8000'

def test_196__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_197__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_198__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test_199__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_200__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_201__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_202__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_203__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_204__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_205__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_206__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test_207__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_208__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_209__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.api.aws'

def test_210__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_211__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_212__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_213__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_214__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_215__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_216__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.api.aws'

def test_217__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_218__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_219__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_220__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_221__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_222__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test_223__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_224__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_225__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_226__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_227__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_228__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_229__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.amazonaws.com'

def test_230__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test_231__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_232__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_233__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.api.aws'

def test_234__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_235__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_236__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_237__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_238__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_239__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_240__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.api.aws'

def test_241__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://333333333333.ddb.us-east-1.amazonaws.com'

def test_242__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://222222222222.ddb.us-east-1.amazonaws.com'

def test_243__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=required, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='required', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_244__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_245__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_246__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_247__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_248__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_249__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_250__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_251__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_252__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_253__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_254__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_255__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_256__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_257__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_258__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_259__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_260__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_261__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_262__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_263__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required and FIPS is enabled, but FIPS account endpoints are not supported')):
        resolve(params)

def test_264__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_265__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_266__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_267__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=required, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='required', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: AccountIdEndpointMode is required but account endpoints are not supported in this partition')):
        resolve(params)

def test_268__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_269__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_270__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test_271__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_272__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_273__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_274__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_275__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_276__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_277__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_278__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_279__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_280__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_281__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test_282__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_283__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_284__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_285__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_286__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.api.aws'

def test_287__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-east-1.amazonaws.com'

def test_288__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.api.aws'

def test_289__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_290__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_291__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=disabled, Region=us-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='disabled', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-east-1.amazonaws.com'

def test_292__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_293__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_294__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_295__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_296__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_297__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_298__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_299__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_300__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_301__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_302__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_303__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_304__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_305__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_306__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_307__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_308__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_309__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_310__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_311__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.cn-north-1.amazonaws.com.cn'

def test_312__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.api.amazonwebservices.com.cn'

def test_313__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_314__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_315__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=cn-north-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='cn-north-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.cn-north-1.amazonaws.com.cn'

def test_316__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test_317__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_318__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test_319__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_320__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_321__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_322__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_323__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_324__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_325__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_326__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_327__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test_328__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_329__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test_330__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_331__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_332__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_333__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_334__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.api.aws.ic.gov'

def test_335__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-iso-east-1.c2s.ic.gov'

def test_336__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.api.aws.ic.gov'

def test_337__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_338__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_339__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=us-iso-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='us-iso-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-iso-east-1.c2s.ic.gov'

def test_340__usefips_true__usedualstack_true__accoun():
    """{UseFIPS=true, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test_341__usefips_true__usedualstack_false__accou():
    """{UseFIPS=true, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_342__usefips_false__usedualstack_true__accou():
    """{UseFIPS=false, UseDualStack=true, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test_343__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_344__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_345__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_346__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_347__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_348__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-west-2:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-west-2:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_349__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=111111111111, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, ResourceArnList=[arn:aws:s3:us-east-1:333333333333:stream/testStream], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='111111111111', ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', ResourceArnList=['arn:aws:s3:us-east-1:333333333333:stream/testStream'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_350__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountId=, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountId='', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_351__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test_352__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_353__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test_354__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_355__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-west-2:222222222222:table/table_name, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-west-2:222222222222:table/table_name', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_356__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:s3:us-west-2:222222222222:stream/testStream, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:s3:us-west-2:222222222222:stream/testStream', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_357__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='', AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_358__usefips_true__usedualstack_true__resour():
    """{UseFIPS=true, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb-fips.us-gov-east-1.api.aws'

def test_359__usefips_true__usedualstack_false__resou():
    """{UseFIPS=true, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=True, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_360__usefips_false__usedualstack_true__resou():
    """{UseFIPS=false, UseDualStack=true, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=True, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.api.aws'

def test_361__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_362__usefips_false__usedualstack_false__reso():
    """{UseFIPS=false, UseDualStack=false, ResourceArn=arn:aws:dynamodb:us-east-1:222222222222:table/table_name, ResourceArnList=[arn:aws:dynamodb:us-east-1:333333333333:table/table_name], AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, ResourceArn='arn:aws:dynamodb:us-east-1:222222222222:table/table_name', ResourceArnList=['arn:aws:dynamodb:us-east-1:333333333333:table/table_name'], AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_363__usefips_false__usedualstack_false__acco():
    """{UseFIPS=false, UseDualStack=false, AccountIdEndpointMode=preferred, Region=us-gov-east-1}"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, AccountIdEndpointMode='preferred', Region='us-gov-east-1')
    result = resolve(params)
    assert result.url == 'https://dynamodb.us-gov-east-1.amazonaws.com'

def test_364__endpoint_https___dynamodb_cn_north_1_ap():
    """{Endpoint=https://dynamodb.cn-north-1.api.amazonwebservices.com.cn, Region=cn-north-1}"""
    params = EndpointParams(Endpoint='https://dynamodb.cn-north-1.api.amazonwebservices.com.cn', Region='cn-north-1')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test_365__endpoint_https___dynamodb_us_gov_east_1():
    """{Endpoint=https://dynamodb.us-gov-east-1.api.aws, Region=us-gov-east-1}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-gov-east-1.api.aws', Region='us-gov-east-1')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test_366__endpoint_https___dynamodb_us_east_1_api():
    """{Endpoint=https://dynamodb.us-east-1.api.aws, Region=us-east-1}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-east-1.api.aws', Region='us-east-1')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test_367__endpoint_https___111111111111_ddb_us_ea():
    """{Endpoint=https://111111111111.ddb.us-east-1.api.aws, Region=us-east-1}"""
    params = EndpointParams(Endpoint='https://111111111111.ddb.us-east-1.api.aws', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://111111111111.ddb.us-east-1.api.aws'

def test_368__endpoint_https___vpce_1a2b3c4d_5e6f_dyn():
    """{Endpoint=https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws, Region=us-east-1}"""
    params = EndpointParams(Endpoint='https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws', Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://vpce-1a2b3c4d-5e6f.dynamodb.us-east-1.vpce.api.aws'

def test_369__endpoint_https___dynamodb_eu_west_1_api():
    """{Endpoint=https://dynamodb.eu-west-1.api.aws, Region=eu-west-1}"""
    params = EndpointParams(Endpoint='https://dynamodb.eu-west-1.api.aws', Region='eu-west-1')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)

def test_370__endpoint_https___dynamodb_us_west_2_api():
    """{Endpoint=https://dynamodb.us-west-2.api.aws, Region=us-west-2}"""
    params = EndpointParams(Endpoint='https://dynamodb.us-west-2.api.aws', Region='us-west-2')
    with pytest.raises(EndpointError, match=re.escape('Endpoint override is not supported for dual-stack endpoints. Please enable dual-stack functionality by enabling the configuration. For more details, see: https://docs.aws.amazon.com/sdkref/latest/guide/feature-endpoints.html')):
        resolve(params)