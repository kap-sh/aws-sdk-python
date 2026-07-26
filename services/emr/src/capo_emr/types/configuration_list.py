"""Generated from Smithy shape ``com.amazonaws.emr#ConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.configuration

ConfigurationList: TypeAlias = list["capo_emr.types.configuration.Configuration"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigurationList) -> list:
    import capo_emr.types.configuration

    out: list = []
    for item in value:
        out.append(capo_emr.types.configuration.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ConfigurationList:
    import capo_emr.types.configuration

    out: ConfigurationList = []
    for item in data:
        out.append(capo_emr.types.configuration.deserialize_aws_json_1_1(item))
    return out
