"""Generated from Smithy shape ``com.amazonaws.interconnect#DescribeConnectionProposalResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_interconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection_bandwidth
    import aws_sdk_interconnect.types.environment_id
    import aws_sdk_interconnect.types.location
    import aws_sdk_interconnect.types.provider


class DescribeConnectionProposalResponse(TypedDict, closed=True):
    bandwidth: "aws_sdk_interconnect.types.connection_bandwidth.ConnectionBandwidth"
    """<p>The bandwidth of the proposed <a>Connection</a>. </p>"""
    environment_id: "aws_sdk_interconnect.types.environment_id.EnvironmentId"
    """<p>The identifier of the <a>Environment</a> upon which the <a>Connection</a> would be placed if this proposal were accepted.</p>"""
    provider: "aws_sdk_interconnect.types.provider.Provider"
    """<p>The partner provider of the specific <a>Environment</a> of the proposal.</p>"""
    location: "aws_sdk_interconnect.types.location.Location"
    """<p>The partner specific location distinguisher of the specific <a>Environment</a> of the proposal.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeConnectionProposalResponse) -> dict:
    out: dict = {}
    out["bandwidth"] = value["bandwidth"]
    out["environmentId"] = value["environment_id"]
    import aws_sdk_interconnect.types.provider

    out["provider"] = aws_sdk_interconnect.types.provider.serialize_aws_json_1_0(
        value["provider"]
    )
    out["location"] = value["location"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeConnectionProposalResponse:
    out: DescribeConnectionProposalResponse = {}  # type: ignore[typeddict-item]
    if "bandwidth" in data:
        out["bandwidth"] = data["bandwidth"]
    else:
        raise DeserializationError(
            "DescribeConnectionProposalResponse.bandwidth required"
        )
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    else:
        raise DeserializationError(
            "DescribeConnectionProposalResponse.environment_id required"
        )
    if "provider" in data:
        import aws_sdk_interconnect.types.provider

        out["provider"] = aws_sdk_interconnect.types.provider.deserialize_aws_json_1_0(
            data["provider"]
        )
    else:
        raise DeserializationError(
            "DescribeConnectionProposalResponse.provider required"
        )
    if "location" in data:
        out["location"] = data["location"]
    else:
        raise DeserializationError(
            "DescribeConnectionProposalResponse.location required"
        )
    return out
