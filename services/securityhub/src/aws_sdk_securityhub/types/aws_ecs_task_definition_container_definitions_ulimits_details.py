"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails(TypedDict, closed=True):
    hard_limit: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The hard limit for the ulimit type.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The type of the ulimit. Valid values are as follows:</p> <ul> <li> <p> <code>core</code> </p> </li> <li> <p> <code>cpu</code> </p> </li> <li> <p> <code>data</code> </p> </li> <li> <p> <code>fsize</code> </p> </li> <li> <p> <code>locks</code> </p> </li> <li> <p> <code>memlock</code> </p> </li> <li> <p> <code>msgqueue</code> </p> </li> <li> <p> <code>nice</code> </p> </li> <li> <p> <code>nofile</code> </p> </li> <li> <p> <code>nproc</code> </p> </li> <li> <p> <code>rss</code> </p> </li> <li> <p> <code>rtprio</code> </p> </li> <li> <p> <code>rttime</code> </p> </li> <li> <p> <code>sigpending</code> </p> </li> <li> <p> <code>stack</code> </p> </li> </ul>"""
    soft_limit: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The soft limit for the ulimit type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails,
) -> dict:
    out: dict = {}
    if "hard_limit" in value:
        out["HardLimit"] = value["hard_limit"]
    if "name" in value:
        out["Name"] = value["name"]
    if "soft_limit" in value:
        out["SoftLimit"] = value["soft_limit"]
    return out


def deserialize_json(
    data: dict,
) -> AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails:
    out: AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails = {}  # type: ignore[typeddict-item]
    if "HardLimit" in data:
        out["hard_limit"] = data["HardLimit"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "SoftLimit" in data:
        out["soft_limit"] = data["SoftLimit"]
    return out
