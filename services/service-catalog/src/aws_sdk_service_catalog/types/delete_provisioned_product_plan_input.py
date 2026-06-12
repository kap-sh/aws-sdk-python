"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.ignore_errors


class DeleteProvisionedProductPlanInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The plan identifier.</p>"""
    ignore_errors: "aws_sdk_service_catalog.types.ignore_errors.IgnoreErrors"
    """<p>If set to true, Service Catalog stops managing the specified provisioned product even if it cannot delete the underlying resources.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanId"] = value["plan_id"]
    out["IgnoreErrors"] = value.get("ignore_errors", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProvisionedProductPlanInput:
    out: DeleteProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PlanId" in data:
        out["plan_id"] = data["PlanId"]
    else:
        raise DeserializationError("DeleteProvisionedProductPlanInput.plan_id required")
    if "IgnoreErrors" in data:
        out["ignore_errors"] = data["IgnoreErrors"]
    else:
        out["ignore_errors"] = False
    return out
