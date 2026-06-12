"""Generated from Smithy shape ``com.amazonaws.ses#VerificationAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.identity
    import aws_sdk_ses.types.identity_verification_attributes

VerificationAttributes: TypeAlias = dict[
    "aws_sdk_ses.types.identity.Identity",
    "aws_sdk_ses.types.identity_verification_attributes.IdentityVerificationAttributes",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: VerificationAttributes,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.identity_verification_attributes

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        aws_sdk_ses.types.identity_verification_attributes.serialize_query(
            value, pairs, f"{prefix}.entry.{n}.value"
        )


def deserialize_query(el: Element) -> VerificationAttributes:
    out: VerificationAttributes = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import aws_sdk_ses.types.identity_verification_attributes

        value = aws_sdk_ses.types.identity_verification_attributes.deserialize_query(
            value_element
        )
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: VerificationAttributes,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import aws_sdk_ses.types.identity_verification_attributes

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        aws_sdk_ses.types.identity_verification_attributes.serialize_query(
            value, pairs, f"{prefix}.{n}.value"
        )


def deserialize_query_flat(parent: Element, tag: str) -> VerificationAttributes:
    out: VerificationAttributes = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import aws_sdk_ses.types.identity_verification_attributes

        value = aws_sdk_ses.types.identity_verification_attributes.deserialize_query(
            value_element
        )
        out[key] = value
    return out
