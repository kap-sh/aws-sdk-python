"""Generated from Smithy shape ``com.amazonaws.iam#GetSAMLProviderResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.assertion_encryption_mode_type
    import aws_sdk_iam.types.date_type
    import aws_sdk_iam.types.private_key_id_type
    import aws_sdk_iam.types.private_key_list
    import aws_sdk_iam.types.saml_metadata_document_type
    import aws_sdk_iam.types.tag_list_type


class GetSAMLProviderResponse(TypedDict, closed=True):
    saml_provider_uuid: NotRequired[
        "aws_sdk_iam.types.private_key_id_type.privateKeyIdType"
    ]
    """<p>The unique identifier assigned to the SAML provider.</p>"""
    saml_metadata_document: NotRequired[
        "aws_sdk_iam.types.saml_metadata_document_type.SAMLMetadataDocumentType"
    ]
    """<p>The XML metadata document that includes information about an identity provider.</p>"""
    create_date: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The date and time when the SAML provider was created.</p>"""
    valid_until: NotRequired["aws_sdk_iam.types.date_type.dateType"]
    """<p>The expiration date and time for the SAML provider.</p>"""
    tags: NotRequired["aws_sdk_iam.types.tag_list_type.tagListType"]
    r"""<p>A list of tags that are attached to the specified IAM SAML provider. The returned list of tags is sorted by tag key. For more information about tagging, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html\">Tagging IAM resources</a> in the <i>IAM User Guide</i>.</p>"""
    assertion_encryption_mode: NotRequired[
        "aws_sdk_iam.types.assertion_encryption_mode_type.assertionEncryptionModeType"
    ]
    """<p>Specifies the encryption setting for the SAML provider.</p>"""
    private_key_list: NotRequired["aws_sdk_iam.types.private_key_list.privateKeyList"]
    """<p>The private key metadata for the SAML provider.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: GetSAMLProviderResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "saml_provider_uuid" in value:
        pairs.append((f"{prefix}.SAMLProviderUUID", str(value["saml_provider_uuid"])))
    if "saml_metadata_document" in value:
        pairs.append(
            (f"{prefix}.SAMLMetadataDocument", str(value["saml_metadata_document"]))
        )
    if "create_date" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["create_date"], pairs, f"{prefix}.CreateDate"
        )
    if "valid_until" in value:
        import aws_sdk_iam.types.date_type

        aws_sdk_iam.types.date_type.serialize_query(
            value["valid_until"], pairs, f"{prefix}.ValidUntil"
        )
    if "tags" in value:
        import aws_sdk_iam.types.tag_list_type

        aws_sdk_iam.types.tag_list_type.serialize_query(
            value["tags"], pairs, f"{prefix}.Tags"
        )
    if "assertion_encryption_mode" in value:
        import aws_sdk_iam.types.assertion_encryption_mode_type

        aws_sdk_iam.types.assertion_encryption_mode_type.serialize_query(
            value["assertion_encryption_mode"],
            pairs,
            f"{prefix}.AssertionEncryptionMode",
        )
    if "private_key_list" in value:
        import aws_sdk_iam.types.private_key_list

        aws_sdk_iam.types.private_key_list.serialize_query(
            value["private_key_list"], pairs, f"{prefix}.PrivateKeyList"
        )


def deserialize_query(el: Element) -> GetSAMLProviderResponse:
    out: GetSAMLProviderResponse = {}  # type: ignore[typeddict-item]
    child_saml_provider_uuid = el.find("SAMLProviderUUID")
    if child_saml_provider_uuid is not None:
        out["saml_provider_uuid"] = str(child_saml_provider_uuid.text or "")
    child_saml_metadata_document = el.find("SAMLMetadataDocument")
    if child_saml_metadata_document is not None:
        out["saml_metadata_document"] = str(child_saml_metadata_document.text or "")
    child_create_date = el.find("CreateDate")
    if child_create_date is not None:
        import aws_sdk_iam.types.date_type

        out["create_date"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_create_date
        )
    child_valid_until = el.find("ValidUntil")
    if child_valid_until is not None:
        import aws_sdk_iam.types.date_type

        out["valid_until"] = aws_sdk_iam.types.date_type.deserialize_query(
            child_valid_until
        )
    child_tags = el.find("Tags")
    if child_tags is not None:
        import aws_sdk_iam.types.tag_list_type

        out["tags"] = aws_sdk_iam.types.tag_list_type.deserialize_query(child_tags)
    child_assertion_encryption_mode = el.find("AssertionEncryptionMode")
    if child_assertion_encryption_mode is not None:
        import aws_sdk_iam.types.assertion_encryption_mode_type

        out["assertion_encryption_mode"] = (
            aws_sdk_iam.types.assertion_encryption_mode_type.deserialize_query(
                child_assertion_encryption_mode
            )
        )
    child_private_key_list = el.find("PrivateKeyList")
    if child_private_key_list is not None:
        import aws_sdk_iam.types.private_key_list

        out["private_key_list"] = aws_sdk_iam.types.private_key_list.deserialize_query(
            child_private_key_list
        )
    return out
