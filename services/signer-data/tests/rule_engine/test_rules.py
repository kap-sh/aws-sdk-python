import pytest
from aws_sdk_signer_data._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_signer_data._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_standard_region_endpoint():
    """Standard region endpoint"""
    params = EndpointParams(Region='us-east-1')
    result = resolve(params)
    assert result.url == 'https://data-signer.us-east-1.amazonaws.com'

def test_european_sovereign_cloud_region_endpoint():
    """European Sovereign Cloud region endpoint"""
    params = EndpointParams(Region='eusc-de-east-1')
    result = resolve(params)
    assert result.url == 'https://data-signer.eusc-de-east-1.amazonaws.eu'

def test_custom_endpoint_override():
    """Custom endpoint override"""
    params = EndpointParams(Region='us-east-1', Endpoint='https://vpce-123.data-signer.us-east-1.vpce.amazonaws.com')
    result = resolve(params)
    assert result.url == 'https://vpce-123.data-signer.us-east-1.vpce.amazonaws.com'

def test_fips_endpoint():
    """FIPS endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://data-signer-fips.us-east-1.amazonaws.com'

def test_dual_stack_endpoint():
    """Dual-stack endpoint"""
    params = EndpointParams(Region='us-east-1', UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://data-signer.us-east-1.api.aws'