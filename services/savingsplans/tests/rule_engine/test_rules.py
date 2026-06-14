import pytest
from aws_sdk_savingsplans._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_savingsplans._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_1_for_region_aws_global_with_fips_disabled():
    """For region aws-global with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='aws-global', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.amazonaws.com'

def test_2_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-east-1.api.aws'

def test_3_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-east-1.amazonaws.com'

def test_4_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.amazonaws.com'

def test_5_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_6_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.cn-north-1.amazonaws.com.cn'

def test_7_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://savingsplans.cn-north-1.api.amazonwebservices.com.cn'

def test_8_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.cn-north-1.amazonaws.com.cn'

def test_9_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-gov-east-1.api.aws'

def test_10_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-gov-east-1.amazonaws.com'

def test_11_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://savingsplans.us-gov-east-1.api.aws'

def test_12_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.us-gov-east-1.amazonaws.com'

def test_13_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-iso-east-1.c2s.ic.gov'

def test_14_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.us-iso-east-1.c2s.ic.gov'

def test_15_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans-fips.us-isob-east-1.sc2s.sgov.gov'

def test_16_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.us-isob-east-1.sc2s.sgov.gov'

def test_17_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_18_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_19_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_20_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test_21_for_region_not_set_with_fips_disabled_an():
    """For region not set with FIPS disabled and DualStack enabled"""
    params = EndpointParams(UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.global.api.aws'

def test_22_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.global.api.aws'

def test_23_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-west-1', UseDualStack=True, UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://savingsplans.global.api.aws'

def test_24_commercial_region_with_custom_sdk_endpoi():
    """Commercial region with custom SDK endpoint"""
    params = EndpointParams(Region='us-east-1', UseDualStack=False, UseFIPS=False, Endpoint='https://custom.example.com')
    result = resolve(params)
    assert result.url == 'https://custom.example.com'