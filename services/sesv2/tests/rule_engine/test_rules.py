import pytest
from capo_sesv2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_sesv2._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_region_af_south_1_with_fips_disabled():
    """For region af-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='af-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.af-south-1.amazonaws.com'

def test_for_region_ap_northeast_1_with_fips_disa():
    """For region ap-northeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-northeast-1.amazonaws.com'

def test_for_region_ap_northeast_2_with_fips_disa():
    """For region ap-northeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-northeast-2.amazonaws.com'

def test_for_region_ap_northeast_3_with_fips_disa():
    """For region ap-northeast-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-northeast-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-northeast-3.amazonaws.com'

def test_for_region_ap_south_1_with_fips_disabled():
    """For region ap-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-south-1.amazonaws.com'

def test_for_region_ap_southeast_1_with_fips_disa():
    """For region ap-southeast-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-southeast-1.amazonaws.com'

def test_for_region_ap_southeast_2_with_fips_disa():
    """For region ap-southeast-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ap-southeast-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ap-southeast-2.amazonaws.com'

def test_for_region_ca_central_1_with_fips_disabl():
    """For region ca-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='ca-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.ca-central-1.amazonaws.com'

def test_for_region_eu_central_1_with_fips_disabl():
    """For region eu-central-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-central-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-central-1.amazonaws.com'

def test_for_region_eu_north_1_with_fips_disabled():
    """For region eu-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-north-1.amazonaws.com'

def test_for_region_eu_south_1_with_fips_disabled():
    """For region eu-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-south-1.amazonaws.com'

def test_for_region_eu_west_1_with_fips_disabled_():
    """For region eu-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-west-1.amazonaws.com'

def test_for_region_eu_west_2_with_fips_disabled_():
    """For region eu-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-west-2.amazonaws.com'

def test_for_region_eu_west_3_with_fips_disabled_():
    """For region eu-west-3 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-west-3', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.eu-west-3.amazonaws.com'

def test_for_region_me_south_1_with_fips_disabled():
    """For region me-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='me-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.me-south-1.amazonaws.com'

def test_for_region_sa_east_1_with_fips_disabled_():
    """For region sa-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='sa-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.sa-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_2_with_fips_disabled_():
    """For region us-east-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-east-2.amazonaws.com'

def test_for_region_us_west_1_with_fips_disabled_():
    """For region us-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-west-1.amazonaws.com'

def test_for_region_us_west_2_with_fips_disabled_():
    """For region us-west-2 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-west-2.amazonaws.com'

def test_for_region_us_west_2_with_fips_enabled_a():
    """For region us-west-2 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-west-2', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-west-2.amazonaws.com'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email.us-east-1.api.aws'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email-fips.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_enabled_():
    """For region cn-north-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.cn-north-1.amazonaws.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email.cn-north-1.api.amazonwebservices.com.cn'

def test_for_region_cn_north_1_with_fips_disabled():
    """For region cn-north-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-north-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.cn-north-1.amazonaws.com.cn'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_enabl():
    """For region us-gov-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-gov-east-1.amazonaws.com'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://email.us-gov-east-1.api.aws'

def test_for_region_us_gov_east_1_with_fips_disab():
    """For region us-gov-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-gov-east-1.amazonaws.com'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email-fips.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://email.us-isob-east-1.sc2s.sgov.gov'

def test_for_custom_endpoint_with_region_set_and_():
    """For custom endpoint with region set and fips disabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled and dualstack disabled"""
    params = EndpointParams(UseFIPS=False, UseDualStack=False, Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled_an():
    """For custom endpoint with fips enabled and dualstack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True, Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test_valid_endpointid_with_dualstack_and_fips():
    """Valid EndpointId with dualstack and FIPS disabled. i.e, IPv4 Only stack with no FIPS"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=False, UseFIPS=False, Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://abc123.456def.endpoints.email.amazonaws.com'

def test_valid_endpointid_with_dualstack_enabled():
    """Valid EndpointId with dualstack enabled"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=True, UseFIPS=False, Region='us-west-2')
    result = resolve(params)
    assert result.url == 'https://abc123.456def.endpoints.email.global.api.aws'

def test_valid_endpointid_with_fips_set__dualstac():
    """Valid EndpointId with FIPS set, dualstack disabled"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=False, UseFIPS=True, Region='ap-northeast-1')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with multi-region endpoints')):
        resolve(params)

def test_valid_endpointid_with_both_dualstack_and():
    """Valid EndpointId with both dualstack and FIPS enabled"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=True, UseFIPS=True, Region='ap-northeast-2')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with multi-region endpoints')):
        resolve(params)

def test_regular_regional_request__without_endpoi():
    """Regular regional request, without EndpointId"""
    params = EndpointParams(UseDualStack=False, Region='eu-west-1')
    result = resolve(params)
    assert result.url == 'https://email.eu-west-1.amazonaws.com'

def test_invalid_endpointid__invalid_chars___form():
    """Invalid EndpointId (Invalid chars / format)"""
    params = EndpointParams(EndpointId='badactor.com?foo=bar', UseDualStack=False, Region='eu-west-2')
    with pytest.raises(EndpointError, match=re.escape('EndpointId must be a valid host label')):
        resolve(params)

def test_invalid_endpointid__empty_():
    """Invalid EndpointId (Empty)"""
    params = EndpointParams(EndpointId='', UseDualStack=False, Region='ap-south-1')
    with pytest.raises(EndpointError, match=re.escape('EndpointId must be a valid host label')):
        resolve(params)

def test_valid_endpointid_with_custom_sdk_endpoin():
    """Valid EndpointId with custom sdk endpoint"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=False, Region='us-east-1', Endpoint='https://example.com')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_valid_endpointid_with_custom_sdk_endpoin():
    """Valid EndpointId with custom sdk endpoint with FIPS enabled"""
    params = EndpointParams(EndpointId='abc123.456def', UseDualStack=False, UseFIPS=True, Region='us-east-1', Endpoint='https://example.com')
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS is not supported with multi-region endpoints')):
        resolve(params)