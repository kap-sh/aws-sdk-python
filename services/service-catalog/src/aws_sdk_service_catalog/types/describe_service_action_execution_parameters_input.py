"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeServiceActionExecutionParametersInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id


class DescribeServiceActionExecutionParametersInput(TypedDict, closed=True):
    provisioned_product_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The identifier of the provisioned product.</p>"""
    service_action_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeServiceActionExecutionParametersInput,
) -> dict:
    out: dict = {}
    out["ProvisionedProductId"] = value["provisioned_product_id"]
    out["ServiceActionId"] = value["service_action_id"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeServiceActionExecutionParametersInput:
    out: DescribeServiceActionExecutionParametersInput = {}  # type: ignore[typeddict-item]
    if "ProvisionedProductId" in data:
        out["provisioned_product_id"] = data["ProvisionedProductId"]
    else:
        raise DeserializationError(
            "DescribeServiceActionExecutionParametersInput.provisioned_product_id required"
        )
    if "ServiceActionId" in data:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        raise DeserializationError(
            "DescribeServiceActionExecutionParametersInput.service_action_id required"
        )
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    return out
