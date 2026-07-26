"""Generated from Smithy shape ``com.amazonaws.iam#summaryMapType``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.summary_key_type
    import capo_iam.types.summary_value_type

summaryMapType: TypeAlias = dict[
    "capo_iam.types.summary_key_type.summaryKeyType",
    "capo_iam.types.summary_value_type.summaryValueType",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: summaryMapType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.summary_key_type

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append(
            (
                f"{prefix}.entry.{n}.key",
                capo_iam.types.summary_key_type.to_query_text(key),
            )
        )
        pairs.append((f"{prefix}.entry.{n}.value", str(value)))


def deserialize_query(el: Element) -> summaryMapType:
    out: summaryMapType = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        import capo_iam.types.summary_key_type

        key = capo_iam.types.summary_key_type.deserialize_query(key_element)
        value = int(str(value_element.text))
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: summaryMapType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_iam.types.summary_key_type

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append(
            (f"{prefix}.{n}.key", capo_iam.types.summary_key_type.to_query_text(key))
        )
        pairs.append((f"{prefix}.{n}.value", str(value)))


def deserialize_query_flat(parent: Element, tag: str) -> summaryMapType:
    out: summaryMapType = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        import capo_iam.types.summary_key_type

        key = capo_iam.types.summary_key_type.deserialize_query(key_element)
        value = int(str(value_element.text))
        out[key] = value
    return out
