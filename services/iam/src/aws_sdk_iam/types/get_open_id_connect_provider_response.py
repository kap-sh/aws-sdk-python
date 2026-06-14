"""Generated from Smithy shape ``com.amazonaws.iam#GetOpenIDConnectProviderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.client_id_list_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.open_id_connect_provider_url_type
    import aws_sdk_iam.types.tag_list_type
    import aws_sdk_iam.types.thumbprint_list_type


class GetOpenIDConnectProviderResponse(TypedDict):
    url: NotRequired[
        "aws_sdk_iam.types.open_id_connect_provider_url_type.OpenIDConnectProviderUrlType"
    ]
    r"""<p>The URL that the IAM OIDC provider resource object is associated with. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html\">CreateOpenIDConnectProvider</a>.</p>"""
    client_id_list: NotRequired[
        "aws_sdk_iam.types.client_id_list_type.clientIDListType"
    ]
    r"""<p>A list of client IDs (also known as audiences) that are associated with the specified IAM OIDC provider resource object. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html\">CreateOpenIDConnectProvider</a>.</p>"""
    thumbprint_list: NotRequired[
        "aws_sdk_iam.types.thumbprint_list_type.thumbprintListType"
    ]
    r"""<p>A list of certificate thumbprints that are associated with the specified IAM OIDC provider resource object. For more information, see <a href=\"https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateOpenIDConnectProvider.html\">CreateOpenIDConnectProvider</a>. </p>"""
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date and time when the IAM OIDC provider resource object was created in the Amazon Web Services account.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    r"""<p>A list of tags that are attached to the specified IAM OIDC provider. The returned list of tags is sorted by tag key. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetOpenIDConnectProviderResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "url" in value:
        pairs.append((f"{prefix}.Url", str(value["url"])))
    if "client_id_list" in value:
        import aws_sdk_iam.types.client_id_list_type

        aws_sdk_iam.types.client_id_list_type.serialize_query(
            value["client_id_list"], pairs, f"{prefix}.ClientIDList"
        )
    if "thumbprint_list" in value:
        import aws_sdk_iam.types.thumbprint_list_type

        aws_sdk_iam.types.thumbprint_list_type.serialize_query(
            value["thumbprint_list"], pairs, f"{prefix}.ThumbprintList"
        )
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )


def deserialize_query(el: Element) -> GetOpenIDConnectProviderResponse:
    out: GetOpenIDConnectProviderResponse = {}  # type: ignore[typeddict-item]
    child_url = el.find("Url")
    if child_url is not None:
        out["url"] = str(child_url.text or "")
    child_client_id_list = el.find("ClientIDList")
    if child_client_id_list is not None:
        import aws_sdk_iam.types.client_id_list_type

        out["client_id_list"] = aws_sdk_iam.types.client_id_list_type.deserialize_query(
            child_client_id_list
        )
    child_thumbprint_list = el.find("ThumbprintList")
    if child_thumbprint_list is not None:
        import aws_sdk_iam.types.thumbprint_list_type

        out["thumbprint_list"] = (
            aws_sdk_iam.types.thumbprint_list_type.deserialize_query(
                child_thumbprint_list
            )
        )
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    return out
