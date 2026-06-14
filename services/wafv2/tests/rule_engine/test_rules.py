import pytest
from aws_sdk_wafv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_wafv2._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_1_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.af-south-1.amazonaws.com'

def test_2_for_region_af_south_1_with_fips_enabled_():
    """For region af-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.af-south-1.amazonaws.com'

def test_3_for_region_ap_east_1_with_fips_disabled_():
    """For region ap-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-east-1.amazonaws.com'

def test_4_for_region_ap_east_1_with_fips_enabled_a():
    """For region ap-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-east-1.amazonaws.com'

def test_5_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-northeast-1.amazonaws.com'

def test_6_for_region_ap_northeast_1_with_fips_enab():
    """For region ap-northeast-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-northeast-1.amazonaws.com'

def test_7_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-northeast-2.amazonaws.com'

def test_8_for_region_ap_northeast_2_with_fips_enab():
    """For region ap-northeast-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-northeast-2.amazonaws.com'

def test_9_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-northeast-3.amazonaws.com'

def test_10_for_region_ap_northeast_3_with_fips_enab():
    """For region ap-northeast-3 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-northeast-3.amazonaws.com'

def test_11_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-south-1.amazonaws.com'

def test_12_for_region_ap_south_1_with_fips_enabled_():
    """For region ap-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-south-1.amazonaws.com'

def test_13_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-southeast-1.amazonaws.com'

def test_14_for_region_ap_southeast_1_with_fips_enab():
    """For region ap-southeast-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-southeast-1.amazonaws.com'

def test_15_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-southeast-2.amazonaws.com'

def test_16_for_region_ap_southeast_2_with_fips_enab():
    """For region ap-southeast-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-southeast-2.amazonaws.com'

def test_17_for_region_ap_southeast_3_with_fips_disa():
    """For region ap-southeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ap-southeast-3.amazonaws.com'

def test_18_for_region_ap_southeast_3_with_fips_enab():
    """For region ap-southeast-3 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-3', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ap-southeast-3.amazonaws.com'

def test_19_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.ca-central-1.amazonaws.com'

def test_20_for_region_ca_central_1_with_fips_enable():
    """For region ca-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.ca-central-1.amazonaws.com'

def test_21_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-central-1.amazonaws.com'

def test_22_for_region_eu_central_1_with_fips_enable():
    """For region eu-central-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-central-1.amazonaws.com'

def test_23_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-north-1.amazonaws.com'

def test_24_for_region_eu_north_1_with_fips_enabled_():
    """For region eu-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-north-1.amazonaws.com'

def test_25_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-south-1.amazonaws.com'

def test_26_for_region_eu_south_1_with_fips_enabled_():
    """For region eu-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-south-1.amazonaws.com'

def test_27_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-west-1.amazonaws.com'

def test_28_for_region_eu_west_1_with_fips_enabled_a():
    """For region eu-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-west-1.amazonaws.com'

def test_29_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-west-2.amazonaws.com'

def test_30_for_region_eu_west_2_with_fips_enabled_a():
    """For region eu-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-west-2.amazonaws.com'

def test_31_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.eu-west-3.amazonaws.com'

def test_32_for_region_eu_west_3_with_fips_enabled_a():
    """For region eu-west-3 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.eu-west-3.amazonaws.com'

def test_33_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.me-south-1.amazonaws.com'

def test_34_for_region_me_south_1_with_fips_enabled_():
    """For region me-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.me-south-1.amazonaws.com'

def test_35_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.sa-east-1.amazonaws.com'

def test_36_for_region_sa_east_1_with_fips_enabled_a():
    """For region sa-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.sa-east-1.amazonaws.com'

def test_37_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-east-1.amazonaws.com'

def test_38_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-east-1.amazonaws.com'

def test_39_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-east-2.amazonaws.com'

def test_40_for_region_us_east_2_with_fips_enabled_a():
    """For region us-east-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-east-2.amazonaws.com'

def test_41_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-west-1.amazonaws.com'

def test_42_for_region_us_west_1_with_fips_enabled_a():
    """For region us-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-west-1.amazonaws.com'

def test_43_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-west-2.amazonaws.com'

def test_44_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-west-2.amazonaws.com'

def test_45_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-east-1.api.aws'

def test_46_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-east-1.api.aws'

def test_47_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.cn-north-1.amazonaws.com.cn'

def test_48_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.cn-north-1.amazonaws.com.cn'

def test_49_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.cn-northwest-1.amazonaws.com.cn'

def test_50_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.cn-northwest-1.amazonaws.com.cn'

def test_51_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_52_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2.cn-north-1.api.amazonwebservices.com.cn'

def test_53_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-gov-east-1.amazonaws.com'

def test_54_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-gov-east-1.amazonaws.com'

def test_55_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-gov-west-1.amazonaws.com'

def test_56_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-gov-west-1.amazonaws.com'

def test_57_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-gov-east-1.api.aws'

def test_58_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-gov-east-1.api.aws'

def test_59_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-iso-east-1.c2s.ic.gov'

def test_60_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-iso-east-1.c2s.ic.gov'

def test_61_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2-fips.us-isob-east-1.sc2s.sgov.gov'

def test_62_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wafv2.us-isob-east-1.sc2s.sgov.gov'

def test_63_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_64_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_65_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_66_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_67_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)