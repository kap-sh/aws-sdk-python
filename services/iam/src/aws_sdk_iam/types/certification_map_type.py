"""Generated from Smithy shape ``com.amazonaws.iam#CertificationMapType``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_iam._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_iam.types.certification_key_type
    import aws_sdk_iam.types.certification_value_type

CertificationMapType: TypeAlias = dict[
    "aws_sdk_iam.types.certification_key_type.CertificationKeyType",
    "aws_sdk_iam.types.certification_value_type.CertificationValueType",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: CertificationMapType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        pairs.append((f"{prefix}.entry.{n}.value", str(value)))


def deserialize_query(el: Element) -> CertificationMapType:
    out: CertificationMapType = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: CertificationMapType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        pairs.append((f"{prefix}.{n}.value", str(value)))


def deserialize_query_flat(parent: Element, tag: str) -> CertificationMapType:
    out: CertificationMapType = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
