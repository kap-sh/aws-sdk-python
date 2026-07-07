"""Generated from Smithy shape ``com.amazonaws.s3#ReplicationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_s3._protocol.xml import Element, SubElement
from aws_sdk_s3.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3.types.replication_rules
    import aws_sdk_s3.types.role


class ReplicationConfiguration(TypedDict, closed=True):
    role: "aws_sdk_s3.types.role.Role"
    r"""<p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that Amazon S3 assumes when replicating objects. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/dev/replication-how-setup.html\">How to Set Up Replication</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    rules: "aws_sdk_s3.types.replication_rules.ReplicationRules"
    """<p>A container for one or more replication rules. A replication configuration must have at least one rule and can contain a maximum of 1,000 rules. </p>"""


# --- restXml ser/de ---
def serialize_xml(value: ReplicationConfiguration, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "Role").text = str(value["role"])
    import aws_sdk_s3.types.replication_rules

    aws_sdk_s3.types.replication_rules.serialize_xml_flat(value["rules"], el, "Rule")


def deserialize_xml(el: Element) -> ReplicationConfiguration:
    out: ReplicationConfiguration = {}  # type: ignore[typeddict-item]
    child_role = el.find("Role")
    if child_role is not None:
        out["role"] = str(child_role.text or "")
    else:
        raise DeserializationError("ReplicationConfiguration.role required")
    if el.find("Rule") is not None:
        import aws_sdk_s3.types.replication_rules

        out["rules"] = aws_sdk_s3.types.replication_rules.deserialize_xml_flat(
            el, "Rule"
        )
    else:
        raise DeserializationError("ReplicationConfiguration.rules required")
    return out
