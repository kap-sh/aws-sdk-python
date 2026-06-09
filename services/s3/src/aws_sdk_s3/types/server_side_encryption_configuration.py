"""Generated from Smithy shape ``com.amazonaws.s3#ServerSideEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.server_side_encryption_rules


class ServerSideEncryptionConfiguration(TypedDict):
    rules: "aws_sdk_s3.types.server_side_encryption_rules.ServerSideEncryptionRules"
    """<p>Container for information about a particular server-side encryption configuration rule.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: ServerSideEncryptionConfiguration, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_s3.types.server_side_encryption_rules

    aws_sdk_s3.types.server_side_encryption_rules.serialize_xml_flat(
        value["rules"], el, "Rule"
    )


def deserialize_xml(el: Element) -> ServerSideEncryptionConfiguration:
    out: ServerSideEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if el.find("Rule") is not None:
        import aws_sdk_s3.types.server_side_encryption_rules

        out["rules"] = (
            aws_sdk_s3.types.server_side_encryption_rules.deserialize_xml_flat(
                el, "Rule"
            )
        )
    else:
        raise DeserializationError("ServerSideEncryptionConfiguration.rules required")
    return out
