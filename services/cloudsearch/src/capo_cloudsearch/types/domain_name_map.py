"""Generated from Smithy shape ``com.amazonaws.cloudsearch#DomainNameMap``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudsearch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudsearch.types.api_version
    import capo_cloudsearch.types.domain_name

DomainNameMap: TypeAlias = dict[
    "capo_cloudsearch.types.domain_name.DomainName",
    "capo_cloudsearch.types.api_version.APIVersion",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: DomainNameMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        pairs.append((f"{prefix}.entry.{n}.value", str(value)))


def deserialize_query(el: Element) -> DomainNameMap:
    out: DomainNameMap = {}
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
    input_to_serialize: DomainNameMap, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        pairs.append((f"{prefix}.{n}.value", str(value)))


def deserialize_query_flat(parent: Element, tag: str) -> DomainNameMap:
    out: DomainNameMap = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        value = str(value_element.text or "")
        out[key] = value
    return out
