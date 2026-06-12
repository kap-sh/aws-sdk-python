"""Generated from Smithy shape ``com.amazonaws.servicecatalog#UpdatePortfolioInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_service_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.accept_language
    import aws_sdk_service_catalog.types.add_tags
    import aws_sdk_service_catalog.types.id
    import aws_sdk_service_catalog.types.portfolio_description
    import aws_sdk_service_catalog.types.portfolio_display_name
    import aws_sdk_service_catalog.types.provider_name
    import aws_sdk_service_catalog.types.tag_keys


class UpdatePortfolioInput(TypedDict):
    accept_language: NotRequired[
        "aws_sdk_service_catalog.types.accept_language.AcceptLanguage"
    ]
    """<p>The language code.</p> <ul> <li> <p> <code>jp</code> - Japanese</p> </li> <li> <p> <code>zh</code> - Chinese</p> </li> </ul>"""
    id: "aws_sdk_service_catalog.types.id.Id"
    """<p>The portfolio identifier.</p>"""
    display_name: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_display_name.PortfolioDisplayName"
    ]
    """<p>The name to use for display purposes.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.portfolio_description.PortfolioDescription"
    ]
    """<p>The updated description of the portfolio.</p>"""
    provider_name: NotRequired[
        "aws_sdk_service_catalog.types.provider_name.ProviderName"
    ]
    """<p>The updated name of the portfolio provider.</p>"""
    add_tags: NotRequired["aws_sdk_service_catalog.types.add_tags.AddTags"]
    """<p>The tags to add.</p>"""
    remove_tags: NotRequired["aws_sdk_service_catalog.types.tag_keys.TagKeys"]
    """<p>The tags to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePortfolioInput) -> dict:
    out: dict = {}
    if "accept_language" in value:
        out["AcceptLanguage"] = value["accept_language"]
    out["Id"] = value["id"]
    if "display_name" in value:
        out["DisplayName"] = value["display_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "provider_name" in value:
        out["ProviderName"] = value["provider_name"]
    if "add_tags" in value:
        import aws_sdk_service_catalog.types.add_tags

        out["AddTags"] = aws_sdk_service_catalog.types.add_tags.serialize_aws_json_1_1(
            value["add_tags"]
        )
    if "remove_tags" in value:
        import aws_sdk_service_catalog.types.tag_keys

        out["RemoveTags"] = (
            aws_sdk_service_catalog.types.tag_keys.serialize_aws_json_1_1(
                value["remove_tags"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePortfolioInput:
    out: UpdatePortfolioInput = {}  # type: ignore[typeddict-item]
    if "AcceptLanguage" in data:
        out["accept_language"] = data["AcceptLanguage"]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdatePortfolioInput.id required")
    if "DisplayName" in data:
        out["display_name"] = data["DisplayName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ProviderName" in data:
        out["provider_name"] = data["ProviderName"]
    if "AddTags" in data:
        import aws_sdk_service_catalog.types.add_tags

        out["add_tags"] = (
            aws_sdk_service_catalog.types.add_tags.deserialize_aws_json_1_1(
                data["AddTags"]
            )
        )
    if "RemoveTags" in data:
        import aws_sdk_service_catalog.types.tag_keys

        out["remove_tags"] = (
            aws_sdk_service_catalog.types.tag_keys.deserialize_aws_json_1_1(
                data["RemoveTags"]
            )
        )
    return out
