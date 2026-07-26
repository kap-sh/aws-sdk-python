"""Generated from Smithy shape ``com.amazonaws.ses#DkimAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ses._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ses.types.identity
    import capo_ses.types.identity_dkim_attributes

DkimAttributes: TypeAlias = dict[
    "capo_ses.types.identity.Identity",
    "capo_ses.types.identity_dkim_attributes.IdentityDkimAttributes",
]


# --- awsQuery ser/de ---
def serialize_query(
    input_to_serialize: DkimAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.identity_dkim_attributes

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.entry.{n}.key", str(key)))
        capo_ses.types.identity_dkim_attributes.serialize_query(
            value, pairs, f"{prefix}.entry.{n}.value"
        )


def deserialize_query(el: Element) -> DkimAttributes:
    out: DkimAttributes = {}
    for entry in el.findall("entry"):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_ses.types.identity_dkim_attributes

        value = capo_ses.types.identity_dkim_attributes.deserialize_query(value_element)
        out[key] = value
    return out


def serialize_query_flat(
    input_to_serialize: DkimAttributes, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_ses.types.identity_dkim_attributes

    for n, (key, value) in enumerate(input_to_serialize.items(), 1):
        pairs.append((f"{prefix}.{n}.key", str(key)))
        capo_ses.types.identity_dkim_attributes.serialize_query(
            value, pairs, f"{prefix}.{n}.value"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DkimAttributes:
    out: DkimAttributes = {}
    for entry in parent.findall(tag):
        key_element = entry.find("key")
        value_element = entry.find("value")
        if key_element is None or value_element is None:
            continue
        key = str(key_element.text or "")
        import capo_ses.types.identity_dkim_attributes

        value = capo_ses.types.identity_dkim_attributes.deserialize_query(value_element)
        out[key] = value
    return out
