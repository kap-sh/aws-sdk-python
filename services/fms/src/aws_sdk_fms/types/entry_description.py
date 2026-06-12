"""Generated from Smithy shape ``com.amazonaws.fms#EntryDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fms.types.entry_type
    import aws_sdk_fms.types.integer_object_minimum0
    import aws_sdk_fms.types.network_acl_entry


class EntryDescription(TypedDict):
    entry_detail: NotRequired["aws_sdk_fms.types.network_acl_entry.NetworkAclEntry"]
    """<p>Describes a rule in a network ACL.</p> <p>Each network ACL has a set of numbered ingress rules and a separate set of numbered egress rules. When determining whether a packet should be allowed in or out of a subnet associated with the network ACL, Amazon Web Services processes the entries in the network ACL according to the rule numbers, in ascending order. </p> <p>When you manage an individual network ACL, you explicitly specify the rule numbers. When you specify the network ACL rules in a Firewall Manager policy, you provide the rules to run first, in the order that you want them to run, and the rules to run last, in the order that you want them to run. Firewall Manager assigns the rule numbers for you when you save the network ACL policy specification.</p>"""
    entry_rule_number: "aws_sdk_fms.types.integer_object_minimum0.IntegerObjectMinimum0"
    """<p>The rule number for the entry. ACL entries are processed in ascending order by rule number. In a Firewall Manager network ACL policy, Firewall Manager assigns rule numbers. </p>"""
    entry_type: NotRequired["aws_sdk_fms.types.entry_type.EntryType"]
    """<p>Specifies whether the entry is managed by Firewall Manager or by a user, and, for Firewall Manager-managed entries, specifies whether the entry is among those that run first in the network ACL or those that run last. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntryDescription) -> dict:
    out: dict = {}
    if "entry_detail" in value:
        import aws_sdk_fms.types.network_acl_entry

        out["EntryDetail"] = aws_sdk_fms.types.network_acl_entry.serialize_aws_json_1_1(
            value["entry_detail"]
        )
    out["EntryRuleNumber"] = value.get("entry_rule_number", 0)
    if "entry_type" in value:
        import aws_sdk_fms.types.entry_type

        out["EntryType"] = aws_sdk_fms.types.entry_type.serialize_aws_json_1_1(
            value["entry_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EntryDescription:
    out: EntryDescription = {}  # type: ignore[typeddict-item]
    if "EntryDetail" in data:
        import aws_sdk_fms.types.network_acl_entry

        out["entry_detail"] = (
            aws_sdk_fms.types.network_acl_entry.deserialize_aws_json_1_1(
                data["EntryDetail"]
            )
        )
    if "EntryRuleNumber" in data:
        out["entry_rule_number"] = data["EntryRuleNumber"]
    else:
        out["entry_rule_number"] = 0
    if "EntryType" in data:
        import aws_sdk_fms.types.entry_type

        out["entry_type"] = aws_sdk_fms.types.entry_type.deserialize_aws_json_1_1(
            data["EntryType"]
        )
    return out
