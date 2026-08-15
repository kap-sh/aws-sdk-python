"""Generated from Smithy shape ``com.amazonaws.iam#mapStringReplacementValueEntry``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_iam._protocol.xml import Element

if TYPE_CHECKING:
    import capo_iam.types.replacement_value_entry
    import capo_iam.types.string_type

mapStringReplacementValueEntry: TypeAlias = dict[
    "capo_iam.types.string_type.stringType",
    "capo_iam.types.replacement_value_entry.ReplacementValueEntry",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: mapStringReplacementValueEntry,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.replacement_value_entry

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        capo_iam.types.replacement_value_entry.serialize_query(
            value, pairs, f"{prefix}.entry.{n}.value"
        )


def deserialize_query(el: Element) -> mapStringReplacementValueEntry:
    out: mapStringReplacementValueEntry = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_iam.types.replacement_value_entry

        value = capo_iam.types.replacement_value_entry.deserialize_query(value_element)
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: mapStringReplacementValueEntry,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_iam.types.replacement_value_entry

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        capo_iam.types.replacement_value_entry.serialize_query(
            value, pairs, f"{prefix}.{n}.value"
        )


def deserialize_query_flat(parent: Element, tag: str) -> mapStringReplacementValueEntry:
    out: mapStringReplacementValueEntry = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_iam.types.replacement_value_entry

        value = capo_iam.types.replacement_value_entry.deserialize_query(value_element)
        out[key] = value
    return out
