"""Generated from Smithy shape ``com.amazonaws.securityhub#EnableSecurityHubV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class EnableSecurityHubV2Response(TypedDict, closed=True):
    hub_v2_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the V2 resource that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnableSecurityHubV2Response) -> dict:
    out: dict = {}
    if "hub_v2_arn" in value:
        out["HubV2Arn"] = value["hub_v2_arn"]
    return out


def deserialize_json(data: dict) -> EnableSecurityHubV2Response:
    out: EnableSecurityHubV2Response = {}  # type: ignore[typeddict-item]
    if "HubV2Arn" in data:
        out["hub_v2_arn"] = data["HubV2Arn"]
    return out
