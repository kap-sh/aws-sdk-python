"""Generated from Smithy shape ``com.amazonaws.invoicing#PutProcurementPortalPreferenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.procurement_portal_preference_arn_string


class PutProcurementPortalPreferenceResponse(TypedDict, closed=True):
    procurement_portal_preference_arn: "aws_sdk_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the updated procurement portal preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutProcurementPortalPreferenceResponse) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutProcurementPortalPreferenceResponse:
    out: PutProcurementPortalPreferenceResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "PutProcurementPortalPreferenceResponse.procurement_portal_preference_arn required"
        )
    return out
