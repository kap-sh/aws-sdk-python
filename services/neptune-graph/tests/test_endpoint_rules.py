
import pytest
from aws_sdk_neptune_graph._rule_engine._endpoint_rule_set import EndpointParams, resolve
from aws_sdk_neptune_graph._rule_engine._endpoint_runtime import EndpointError
import re
import zapros


def test_1_region_and_cp_apitype_are_provided():
    """Region and CP ApiType are provided"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='ControlPlane',
        Region='us-east-1',
    )

    result = resolve(params)
    assert result.url == 'https://mycustomDomain.com'


def test_2_region_and_dp_apitype_are_provided():
    """Region and DP ApiType are provided"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='DataPlane',
        Region='us-east-1',
    )

    result = resolve(params)
    assert result.url == 'https://mycustomDomain.com'


def test_3_region_and_invalid_apitype_are_provided():
    """Region and invalid ApiType are provided"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='someInvalidApiType',
        Region='us-east-1',
    )

    result = resolve(params)
    assert result.url == 'https://mycustomDomain.com'


def test_4_only_invalid_apitype_is_provided():
    """Only invalid ApiType is provided"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='someInvalidApiType',
    )

    result = resolve(params)
    assert result.url == 'https://mycustomDomain.com'


def test_5_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-east-1.api.aws'


def test_6_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_7_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-east-1.amazonaws.com'


def test_8_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_9_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-1.api.aws'


def test_10_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-1.on.aws'


def test_11_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-1.amazonaws.com'


def test_12_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://us-east-1.neptune-graph.amazonaws.com'


def test_13_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-east-2.api.aws'


def test_14_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_15_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-east-2.amazonaws.com'


def test_16_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_17_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-2.api.aws'


def test_18_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-2.on.aws'


def test_19_validate_cp_endpoint_in_region__us_east_():
    """Validate CP endpoint in region: us-east-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-east-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-east-2.amazonaws.com'


def test_20_validate_dp_endpoint_in_region__us_east_():
    """Validate DP endpoint in region: us-east-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-east-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://us-east-2.neptune-graph.amazonaws.com'


def test_21_validate_cp_endpoint_in_region__us_west_():
    """Validate CP endpoint in region: us-west-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-west-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-west-2.api.aws'


def test_22_validate_dp_endpoint_in_region__us_west_():
    """Validate DP endpoint in region: us-west-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-west-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_23_validate_cp_endpoint_in_region__us_west_():
    """Validate CP endpoint in region: us-west-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-west-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.us-west-2.amazonaws.com'


def test_24_validate_dp_endpoint_in_region__us_west_():
    """Validate DP endpoint in region: us-west-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-west-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_25_validate_cp_endpoint_in_region__us_west_():
    """Validate CP endpoint in region: us-west-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-west-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-west-2.api.aws'


def test_26_validate_dp_endpoint_in_region__us_west_():
    """Validate DP endpoint in region: us-west-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-west-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-west-2.on.aws'


def test_27_validate_cp_endpoint_in_region__us_west_():
    """Validate CP endpoint in region: us-west-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='us-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.us-west-2.amazonaws.com'


def test_28_validate_dp_endpoint_in_region__us_west_():
    """Validate DP endpoint in region: us-west-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='us-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://us-west-2.neptune-graph.amazonaws.com'


def test_29_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-west-1.api.aws'


def test_30_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_31_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-west-1.amazonaws.com'


def test_32_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_33_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-1.api.aws'


def test_34_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-1.on.aws'


def test_35_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-1.amazonaws.com'


def test_36_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://eu-west-1.neptune-graph.amazonaws.com'


def test_37_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-west-2.api.aws'


def test_38_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-2, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-2',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_39_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-west-2.amazonaws.com'


def test_40_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-2, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-2',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_41_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-2.api.aws'


def test_42_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-2, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-2',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-2.on.aws'


def test_43_validate_cp_endpoint_in_region__eu_west_():
    """Validate CP endpoint in region: eu-west-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-west-2.amazonaws.com'


def test_44_validate_dp_endpoint_in_region__eu_west_():
    """Validate DP endpoint in region: eu-west-2, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-west-2',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://eu-west-2.neptune-graph.amazonaws.com'


def test_45_validate_cp_endpoint_in_region__eu_centr():
    """Validate CP endpoint in region: eu-central-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-central-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-central-1.api.aws'


def test_46_validate_dp_endpoint_in_region__eu_centr():
    """Validate DP endpoint in region: eu-central-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-central-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_47_validate_cp_endpoint_in_region__eu_centr():
    """Validate CP endpoint in region: eu-central-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-central-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.eu-central-1.amazonaws.com'


def test_48_validate_dp_endpoint_in_region__eu_centr():
    """Validate DP endpoint in region: eu-central-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-central-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_49_validate_cp_endpoint_in_region__eu_centr():
    """Validate CP endpoint in region: eu-central-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-central-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-central-1.api.aws'


def test_50_validate_dp_endpoint_in_region__eu_centr():
    """Validate DP endpoint in region: eu-central-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-central-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-central-1.on.aws'


def test_51_validate_cp_endpoint_in_region__eu_centr():
    """Validate CP endpoint in region: eu-central-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='eu-central-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.eu-central-1.amazonaws.com'


def test_52_validate_dp_endpoint_in_region__eu_centr():
    """Validate DP endpoint in region: eu-central-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='eu-central-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://eu-central-1.neptune-graph.amazonaws.com'


def test_53_validate_cp_endpoint_in_region__ap_south():
    """Validate CP endpoint in region: ap-southeast-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-southeast-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.ap-southeast-1.api.aws'


def test_54_validate_dp_endpoint_in_region__ap_south():
    """Validate DP endpoint in region: ap-southeast-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-southeast-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_55_validate_cp_endpoint_in_region__ap_south():
    """Validate CP endpoint in region: ap-southeast-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-southeast-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.ap-southeast-1.amazonaws.com'


def test_56_validate_dp_endpoint_in_region__ap_south():
    """Validate DP endpoint in region: ap-southeast-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-southeast-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_57_validate_cp_endpoint_in_region__ap_south():
    """Validate CP endpoint in region: ap-southeast-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-southeast-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-southeast-1.api.aws'


def test_58_validate_dp_endpoint_in_region__ap_south():
    """Validate DP endpoint in region: ap-southeast-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-southeast-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-southeast-1.on.aws'


def test_59_validate_cp_endpoint_in_region__ap_south():
    """Validate CP endpoint in region: ap-southeast-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-southeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-southeast-1.amazonaws.com'


def test_60_validate_dp_endpoint_in_region__ap_south():
    """Validate DP endpoint in region: ap-southeast-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-southeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://ap-southeast-1.neptune-graph.amazonaws.com'


def test_61_validate_cp_endpoint_in_region__ap_north():
    """Validate CP endpoint in region: ap-northeast-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-northeast-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.ap-northeast-1.api.aws'


def test_62_validate_dp_endpoint_in_region__ap_north():
    """Validate DP endpoint in region: ap-northeast-1, useFipsEndpoint: true, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-northeast-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_63_validate_cp_endpoint_in_region__ap_north():
    """Validate CP endpoint in region: ap-northeast-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-northeast-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph-fips.ap-northeast-1.amazonaws.com'


def test_64_validate_dp_endpoint_in_region__ap_north():
    """Validate DP endpoint in region: ap-northeast-1, useFipsEndpoint: true, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-northeast-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: fips endpoint is not supported for this API')):
        resolve(params)


def test_65_validate_cp_endpoint_in_region__ap_north():
    """Validate CP endpoint in region: ap-northeast-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-northeast-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-northeast-1.api.aws'


def test_66_validate_dp_endpoint_in_region__ap_north():
    """Validate DP endpoint in region: ap-northeast-1, useFipsEndpoint: false, useDualStackEndpoint: true"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-northeast-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-northeast-1.on.aws'


def test_67_validate_cp_endpoint_in_region__ap_north():
    """Validate CP endpoint in region: ap-northeast-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='ControlPlane',
        Region='ap-northeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://neptune-graph.ap-northeast-1.amazonaws.com'


def test_68_validate_dp_endpoint_in_region__ap_north():
    """Validate DP endpoint in region: ap-northeast-1, useFipsEndpoint: false, useDualStackEndpoint: false"""
    params = EndpointParams(
        ApiType='DataPlane',
        Region='ap-northeast-1',
        UseFIPS=False,
        UseDualStack=False,
    )

    result = resolve(params)
    assert result.url == 'https://ap-northeast-1.neptune-graph.amazonaws.com'


def test_69_validate_when_no_region_is_provided():
    """Validate When no region is provided"""
    params = EndpointParams(
        ApiType='DataPlane',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)


def test_70_validate_when_invalid_unknown_apitype_pr():
    """Validate When invalid/unknown ApiType provided"""
    params = EndpointParams(
        Region='us-east-1',
        ApiType='someUnknownValue',
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Unknown ApiType')):
        resolve(params)


def test_71_both_fips_and_dualstack_enabled():
    """Both Fips and dualstack enabled"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


def test_72_fips_enabled_and_dualstack_disabled():
    """Fips enabled and dualstack disabled"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=True,
        UseDualStack=False,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)


def test_73_fips_disabled_and_dualstack_enabled():
    """Fips disabled and dualstack enabled"""
    params = EndpointParams(
        Endpoint='https://mycustomDomain.com',
        ApiType='ControlPlane',
        Region='us-east-1',
        UseFIPS=False,
        UseDualStack=True,
    )

    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)


