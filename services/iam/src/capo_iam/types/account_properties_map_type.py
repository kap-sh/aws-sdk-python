"""Generated from Smithy shape ``com.amazonaws.iam#accountPropertiesMapType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.account_property_key_type
    import capo_iam.types.account_property_value_type

accountPropertiesMapType: TypeAlias = dict[
    "capo_iam.types.account_property_key_type.accountPropertyKeyType",
    "capo_iam.types.account_property_value_type.accountPropertyValueType",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: accountPropertiesMapType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        pairs.append((f"{prefix}.entry.{n}.value", str(value)))


def deserialize_query(el: Element) -> accountPropertiesMapType:
    out: accountPropertiesMapType = {}
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
    input_to_serialize: accountPropertiesMapType,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        pairs.append((f"{prefix}.{n}.value", str(value)))


def deserialize_query_flat(parent: Element, tag: str) -> accountPropertiesMapType:
    out: accountPropertiesMapType = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
