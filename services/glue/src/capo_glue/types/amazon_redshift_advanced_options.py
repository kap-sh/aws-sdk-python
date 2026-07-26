"""Generated from Smithy shape ``com.amazonaws.glue#AmazonRedshiftAdvancedOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.amazon_redshift_advanced_option

AmazonRedshiftAdvancedOptions: TypeAlias = list[
    "capo_glue.types.amazon_redshift_advanced_option.AmazonRedshiftAdvancedOption"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AmazonRedshiftAdvancedOptions) -> list:
    import capo_glue.types.amazon_redshift_advanced_option

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.amazon_redshift_advanced_option.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AmazonRedshiftAdvancedOptions:
    import capo_glue.types.amazon_redshift_advanced_option

    out: AmazonRedshiftAdvancedOptions = []
    for item in data:
        out.append(
            capo_glue.types.amazon_redshift_advanced_option.deserialize_aws_json_1_1(
                item
            )
        )
    return out
