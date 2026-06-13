"""Generated from Smithy shape ``com.amazonaws.invoicing#GetProcurementPortalPreferenceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.procurement_portal_preference_arn_string


class GetProcurementPortalPreferenceRequest(TypedDict):
    procurement_portal_preference_arn: "aws_sdk_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProcurementPortalPreferenceRequest) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProcurementPortalPreferenceRequest:
    out: GetProcurementPortalPreferenceRequest = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "GetProcurementPortalPreferenceRequest.procurement_portal_preference_arn required"
        )
    return out
