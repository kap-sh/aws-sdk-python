"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#StartChangeSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_marketplace_catalog.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_catalog.types.catalog
    import aws_sdk_marketplace_catalog.types.change_set_name
    import aws_sdk_marketplace_catalog.types.client_request_token
    import aws_sdk_marketplace_catalog.types.intent
    import aws_sdk_marketplace_catalog.types.requested_change_list
    import aws_sdk_marketplace_catalog.types.tag_list


class StartChangeSetRequest(TypedDict, closed=True):
    catalog: "aws_sdk_marketplace_catalog.types.catalog.Catalog"
    """<p>The catalog related to the request. Fixed value: <code>AWSMarketplace</code> </p>"""
    change_set: (
        "aws_sdk_marketplace_catalog.types.requested_change_list.RequestedChangeList"
    )
    """<p>Array of <code>change</code> object.</p>"""
    change_set_name: NotRequired[
        "aws_sdk_marketplace_catalog.types.change_set_name.ChangeSetName"
    ]
    """<p>Optional case sensitive string of up to 100 ASCII characters. The change set name can be used to filter the list of change sets. </p>"""
    client_request_token: NotRequired[
        "aws_sdk_marketplace_catalog.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique token to identify the request to ensure idempotency.</p>"""
    change_set_tags: NotRequired["aws_sdk_marketplace_catalog.types.tag_list.TagList"]
    """<p>A list of objects specifying each key name and value for the <code>ChangeSetTags</code> property.</p>"""
    intent: NotRequired["aws_sdk_marketplace_catalog.types.intent.Intent"]
    r"""<p>The intent related to the request. The default is <code>APPLY</code>. To test your request before applying changes to your entities, use <code>VALIDATE</code>. This feature is currently available for adding versions to single-AMI products. For more information, see <a href=\"https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/ami-products.html#ami-add-version\">Add a new version</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartChangeSetRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    import aws_sdk_marketplace_catalog.types.requested_change_list

    out["ChangeSet"] = (
        aws_sdk_marketplace_catalog.types.requested_change_list.serialize_json(
            value["change_set"]
        )
    )
    if "change_set_name" in value:
        out["ChangeSetName"] = value["change_set_name"]
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "change_set_tags" in value:
        import aws_sdk_marketplace_catalog.types.tag_list

        out["ChangeSetTags"] = (
            aws_sdk_marketplace_catalog.types.tag_list.serialize_json(
                value["change_set_tags"]
            )
        )
    if "intent" in value:
        import aws_sdk_marketplace_catalog.types.intent

        out["Intent"] = aws_sdk_marketplace_catalog.types.intent.serialize_json(
            value["intent"]
        )
    return out


def deserialize_json(data: dict) -> StartChangeSetRequest:
    out: StartChangeSetRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("StartChangeSetRequest.catalog required")
    if "ChangeSet" in data:
        import aws_sdk_marketplace_catalog.types.requested_change_list

        out["change_set"] = (
            aws_sdk_marketplace_catalog.types.requested_change_list.deserialize_json(
                data["ChangeSet"]
            )
        )
    else:
        raise DeserializationError("StartChangeSetRequest.change_set required")
    if "ChangeSetName" in data:
        out["change_set_name"] = data["ChangeSetName"]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "ChangeSetTags" in data:
        import aws_sdk_marketplace_catalog.types.tag_list

        out["change_set_tags"] = (
            aws_sdk_marketplace_catalog.types.tag_list.deserialize_json(
                data["ChangeSetTags"]
            )
        )
    if "Intent" in data:
        import aws_sdk_marketplace_catalog.types.intent

        out["intent"] = aws_sdk_marketplace_catalog.types.intent.deserialize_json(
            data["Intent"]
        )
    return out
