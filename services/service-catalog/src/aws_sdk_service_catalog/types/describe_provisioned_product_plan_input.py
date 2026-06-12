"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisionedProductPlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class DescribeProvisionedProductPlanInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    plan_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The plan identifier.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisionedProductPlanInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["PlanId"] = value["plan_id"]
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisionedProductPlanInput:
    out: DescribeProvisionedProductPlanInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "PlanId" in data:
        out["plan_id"] = data["PlanId"]
    else:
        raise DeserializationError(
            "DescribeProvisionedProductPlanInput.plan_id required"
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    return out
