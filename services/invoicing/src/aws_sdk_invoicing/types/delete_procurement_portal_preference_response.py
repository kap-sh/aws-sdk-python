"""Generated from Smithy shape ``com.amazonaws.invoicing#DeleteProcurementPortalPreferenceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.procurement_portal_preference_arn_string


class DeleteProcurementPortalPreferenceResponse(TypedDict):
    procurement_portal_preference_arn: "aws_sdk_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the deleted procurement portal preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProcurementPortalPreferenceResponse) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProcurementPortalPreferenceResponse:
    out: DeleteProcurementPortalPreferenceResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "DeleteProcurementPortalPreferenceResponse.procurement_portal_preference_arn required"
        )
    return out
