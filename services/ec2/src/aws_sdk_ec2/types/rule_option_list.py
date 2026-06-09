"""Generated from Smithy shape ``com.amazonaws.ec2#RuleOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.rule_option

RuleOptionList: TypeAlias = list["aws_sdk_ec2.types.rule_option.RuleOption"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RuleOptionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.rule_option

        aws_sdk_ec2.types.rule_option.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(parent: Element, tag: str) -> RuleOptionList:
    import aws_sdk_ec2.types.rule_option

    out: RuleOptionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.rule_option.deserialize_ec2_query(child))
    return out
