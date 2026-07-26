"""Generated from Smithy shape ``com.amazonaws.s3#JournalTableConfigurationUpdates``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3._protocol.xml import Element, SubElement
from capo_s3.errors import DeserializationError

if TYPE_CHECKING:
    import capo_s3.types.record_expiration


class JournalTableConfigurationUpdates(TypedDict, closed=True):
    record_expiration: "capo_s3.types.record_expiration.RecordExpiration"
    """<p> The journal table record expiration settings for the journal table. </p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: JournalTableConfigurationUpdates, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_s3.types.record_expiration

    capo_s3.types.record_expiration.serialize_xml(
        value["record_expiration"], el, "RecordExpiration"
    )


def deserialize_xml(el: Element) -> JournalTableConfigurationUpdates:
    out: JournalTableConfigurationUpdates = {}  # type: ignore[typeddict-item]
    child_record_expiration = el.find("RecordExpiration")
    if child_record_expiration is not None:
        import capo_s3.types.record_expiration

        out["record_expiration"] = capo_s3.types.record_expiration.deserialize_xml(
            child_record_expiration
        )
    else:
        raise DeserializationError(
            "JournalTableConfigurationUpdates.record_expiration required"
        )
    return out
