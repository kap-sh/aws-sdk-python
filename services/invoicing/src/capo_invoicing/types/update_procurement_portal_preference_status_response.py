"""Generated from Smithy shape ``com.amazonaws.invoicing#UpdateProcurementPortalPreferenceStatusResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.procurement_portal_preference_arn_string


class UpdateProcurementPortalPreferenceStatusResponse(TypedDict, closed=True):
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference with updated status.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: UpdateProcurementPortalPreferenceStatusResponse,
) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> UpdateProcurementPortalPreferenceStatusResponse:
    out: UpdateProcurementPortalPreferenceStatusResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "UpdateProcurementPortalPreferenceStatusResponse.procurement_portal_preference_arn required"
        )
    return out
