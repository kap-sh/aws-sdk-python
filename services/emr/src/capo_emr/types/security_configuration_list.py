"""Generated from Smithy shape ``com.amazonaws.emr#SecurityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.security_configuration_summary

SecurityConfigurationList: TypeAlias = list[
    "capo_emr.types.security_configuration_summary.SecurityConfigurationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityConfigurationList) -> list:
    import capo_emr.types.security_configuration_summary

    out: list = []
    for item in value:
        out.append(
            capo_emr.types.security_configuration_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SecurityConfigurationList:
    import capo_emr.types.security_configuration_summary

    out: SecurityConfigurationList = []
    for item in data:
        out.append(
            capo_emr.types.security_configuration_summary.deserialize_aws_json_1_1(item)
        )
    return out
