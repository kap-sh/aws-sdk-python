"""Generated from Smithy shape ``com.amazonaws.emrcontainers#DescribeSecurityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.resource_id_string


class DescribeSecurityConfigurationRequest(TypedDict, closed=True):
    id: "aws_sdk_emr_containers.types.resource_id_string.ResourceIdString"
    """<p>The ID of the security configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeSecurityConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeSecurityConfigurationRequest:
    out: DescribeSecurityConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
