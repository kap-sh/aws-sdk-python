"""Generated from Smithy shape ``com.amazonaws.inspector#RulesPackageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector.types.rules_package

RulesPackageList: TypeAlias = list["aws_sdk_inspector.types.rules_package.RulesPackage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RulesPackageList) -> list:
    import aws_sdk_inspector.types.rules_package

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector.types.rules_package.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> RulesPackageList:
    import aws_sdk_inspector.types.rules_package

    out: RulesPackageList = []
    for item in data:
        out.append(aws_sdk_inspector.types.rules_package.deserialize_aws_json_1_1(item))
    return out
