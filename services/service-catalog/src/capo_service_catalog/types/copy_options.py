"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyOptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.copy_option

CopyOptions: TypeAlias = list["capo_service_catalog.types.copy_option.CopyOption"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyOptions) -> list:
    import capo_service_catalog.types.copy_option

    out: list = []
    for item in value:
        out.append(capo_service_catalog.types.copy_option.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CopyOptions:
    import capo_service_catalog.types.copy_option

    out: CopyOptions = []
    for item in data:
        out.append(
            capo_service_catalog.types.copy_option.deserialize_aws_json_1_1(item)
        )
    return out
