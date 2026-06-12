"""Generated from Smithy shape ``com.amazonaws.emr#NewSupportedProductsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.supported_product_config

NewSupportedProductsList: TypeAlias = list[
    "aws_sdk_emr.types.supported_product_config.SupportedProductConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NewSupportedProductsList) -> list:
    import aws_sdk_emr.types.supported_product_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.supported_product_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NewSupportedProductsList:
    import aws_sdk_emr.types.supported_product_config

    out: NewSupportedProductsList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.supported_product_config.deserialize_aws_json_1_1(item)
        )
    return out
