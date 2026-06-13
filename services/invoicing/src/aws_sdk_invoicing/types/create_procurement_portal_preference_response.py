"""Generated from Smithy shape ``com.amazonaws.invoicing#CreateProcurementPortalPreferenceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.procurement_portal_preference_arn_string


class CreateProcurementPortalPreferenceResponse(TypedDict):
    procurement_portal_preference_arn: "aws_sdk_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the created procurement portal preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProcurementPortalPreferenceResponse) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProcurementPortalPreferenceResponse:
    out: CreateProcurementPortalPreferenceResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "CreateProcurementPortalPreferenceResponse.procurement_portal_preference_arn required"
        )
    return out
