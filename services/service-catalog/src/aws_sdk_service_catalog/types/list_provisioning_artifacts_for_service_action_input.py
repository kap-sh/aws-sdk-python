"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ListProvisioningArtifactsForServiceActionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.page_size
    import aws_sdk_service_catalog.types.page_token


class ListProvisioningArtifactsForServiceActionInput(TypedDict):
    service_action_id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The self-service action identifier. For example, <code>act-fs7abcd89wxyz</code>.</p>"""
    page_size: "aws_sdk_service_catalog.types.page_size.PageSize"
    """<p>The maximum number of items to return with this call.</p>"""
    page_token: NotRequired["aws_sdk_service_catalog.types.page_token.PageToken"]
    """<p>The page token for the next set of results. To retrieve the first set of results, use null.</p>"""
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListProvisioningArtifactsForServiceActionInput,
) -> dict:
    out: dict = {}
    out["ServiceActionId"] = value["service_action_id"]
    out["PageSize"] = value.get("page_size", 0)
    if "page_token" in value:
        out["PageToken"] = value["page_token"]
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListProvisioningArtifactsForServiceActionInput:
    out: ListProvisioningArtifactsForServiceActionInput = {}  # type: ignore[typeddict-item]
    if "ServiceActionId" in data:
        out["service_action_id"] = data["ServiceActionId"]
    else:
        raise DeserializationError(
            "ListProvisioningArtifactsForServiceActionInput.service_action_id required"
        )
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    else:
        out["page_size"] = 0
    if "PageToken" in data:
        out["page_token"] = data["PageToken"]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    return out
