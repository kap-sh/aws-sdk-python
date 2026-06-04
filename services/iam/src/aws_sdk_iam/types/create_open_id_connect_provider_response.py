"""Generated from Smithy shape ``com.amazonaws.iam#CreateOpenIDConnectProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.arn_type
    import aws_sdk_iam.types.tag_list_type


class CreateOpenIDConnectProviderResponse(TypedDict):
    open_id_connect_provider_arn: NotRequired["aws_sdk_iam.types.arn_type.arnType"]
    """<p>The Amazon Resource Name (ARN) of the new IAM OpenID Connect provider that is created. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_OpenIDConnectProviderListEntry.html\">OpenIDConnectProviderListEntry</a>. </p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    """<p>A list of tags that are attached to the new IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateOpenIDConnectProviderResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "open_id_connect_provider_arn" in value:
        pairs.append(
            (
                f"{prefix}.OpenIDConnectProviderArn",
                str(value["open_id_connect_provider_arn"]),
            )
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> CreateOpenIDConnectProviderResponse:
    out: CreateOpenIDConnectProviderResponse = {}  # type: ignore[typeddict-item]
    child_open_id_connect_provider_arn = el.find("OpenIDConnectProviderArn")
    if child_open_id_connect_provider_arn is not None:
        out["open_id_connect_provider_arn"] = str(
            child_open_id_connect_provider_arn.text or ""
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
