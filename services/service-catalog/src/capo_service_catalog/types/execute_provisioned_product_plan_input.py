"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ExecuteProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import capo_service_catalog.types.accept_language
    import capo_service_catalog.types.id
    import capo_service_catalog.types.idempotency_token


class ExecuteProvisionedProductPlanInput(TypedDict, closed=True):
    accept_language: NotRequired[
        "capo_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_id: "capo_service_catalog.types.id.Id"
    """<p>The plan identifier.</p>"""
    idempotency_token: "capo_service_catalog.types.idempotency_token.IdempotencyToken"
    """<p>A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token, the same response is returned for each repeated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecuteProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanId"] = value["plan_id"]
    out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecuteProvisionedProductPlanInput:
    out: ExecuteProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PlanId" in data:
        out["plan_id"] = data["PlanId"]
    else:
        raise DeserializationError(
            "ExecuteProvisionedProductPlanInput.plan_id required"
        )
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    else:
        raise DeserializationError(
            "ExecuteProvisionedProductPlanInput.idempotency_token required"
        )
    return out
