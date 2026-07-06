"""Generated from Smithy shape ``com.amazonaws.quicksight#CreateNamespaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.identity_store
    import aws_sdk_quicksight.types.namespace
    import aws_sdk_quicksight.types.tag_list


class CreateNamespaceRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID for the Amazon Web Services account that you want to create the Quick Sight namespace in.</p>"""
    namespace: "aws_sdk_quicksight.types.namespace.Namespace"
    """<p>The name that you want to use to describe the new namespace.</p>"""
    identity_store: "aws_sdk_quicksight.types.identity_store.IdentityStore"
    """<p>Specifies the type of your user identity directory. Currently, this supports users with an identity type of <code>QUICKSIGHT</code>.</p>"""
    tags: NotRequired["aws_sdk_quicksight.types.tag_list.TagList"]
    """<p>The tags that you want to associate with the namespace that you're creating.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNamespaceRequest) -> dict:
    out: dict = {}
    out["Namespace"] = value["namespace"]
    import aws_sdk_quicksight.types.identity_store

    out["IdentityStore"] = aws_sdk_quicksight.types.identity_store.serialize_json(
        value["identity_store"]
    )
    if "tags" in value:
        import aws_sdk_quicksight.types.tag_list

        out["Tags"] = aws_sdk_quicksight.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateNamespaceRequest:
    out: CreateNamespaceRequest = {}  # type: ignore[typeddict-item]
    if "Namespace" in data:
        out["namespace"] = data["Namespace"]
    else:
        raise DeserializationError("CreateNamespaceRequest.namespace required")
    if "IdentityStore" in data:
        import aws_sdk_quicksight.types.identity_store

        out["identity_store"] = (
            aws_sdk_quicksight.types.identity_store.deserialize_json(
                data["IdentityStore"]
            )
        )
    else:
        raise DeserializationError("CreateNamespaceRequest.identity_store required")
    if "Tags" in data:
        import aws_sdk_quicksight.types.tag_list

        out["tags"] = aws_sdk_quicksight.types.tag_list.deserialize_json(data["Tags"])
    return out
