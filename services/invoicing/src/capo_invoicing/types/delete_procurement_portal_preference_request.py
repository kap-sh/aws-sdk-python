"""Generated from Smithy shape ``com.amazonaws.invoicing#DeleteProcurementPortalPreferenceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.basic_string_without_space
    import capo_invoicing.types.procurement_portal_preference_arn_string


class DeleteProcurementPortalPreferenceRequest(TypedDict, closed=True):
    procurement_portal_preference_arn: "capo_invoicing.types.procurement_portal_preference_arn_string.ProcurementPortalPreferenceArnString"
    """<p>The Amazon Resource Name (ARN) of the procurement portal preference to delete.</p>"""
    client_token: NotRequired[
        "capo_invoicing.types.basic_string_without_space.BasicStringWithoutSpace"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure idempotency of the request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProcurementPortalPreferenceRequest) -> dict:
    out: dict = {}
    out["ProcurementPortalPreferenceArn"] = value["procurement_portal_preference_arn"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProcurementPortalPreferenceRequest:
    out: DeleteProcurementPortalPreferenceRequest = {}  # type: ignore[typeddict-item]
    if "ProcurementPortalPreferenceArn" in data:
        out["procurement_portal_preference_arn"] = data[
            "ProcurementPortalPreferenceArn"
        ]
    else:
        raise DeserializationError(
            "DeleteProcurementPortalPreferenceRequest.procurement_portal_preference_arn required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
