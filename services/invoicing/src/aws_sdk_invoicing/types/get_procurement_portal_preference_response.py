"""Generated from Smithy shape ``com.amazonaws.invoicing#GetProcurementPortalPreferenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_invoicing.types.procurement_portal_preference


class GetProcurementPortalPreferenceResponse(TypedDict, closed=True):
    procurement_portal_preference: "aws_sdk_invoicing.types.procurement_portal_preference.ProcurementPortalPreference"
    """<p>The detailed configuration of the requested procurement portal preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProcurementPortalPreferenceResponse) -> dict:
    out: dict = {}
    import aws_sdk_invoicing.types.procurement_portal_preference

    out["ProcurementPortalPreference"] = (
        aws_sdk_invoicing.types.procurement_portal_preference.serialize_aws_json_1_0(
            value["procurement_portal_preference"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProcurementPortalPreferenceResponse:
    out: GetProcurementPortalPreferenceResponse = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreference" in data:
        import aws_sdk_invoicing.types.procurement_portal_preference

        out["procurement_portal_preference"] = (
            aws_sdk_invoicing.types.procurement_portal_preference.deserialize_aws_json_1_0(
                data["ProcurementPortalPreference"]
            )
        )
    else:
        raise DeserializationError(
            "GetProcurementPortalPreferenceResponse.procurement_portal_preference required"
        )
    return out
