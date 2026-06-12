"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeDetailMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_account.types.connection_type
    import aws_sdk_partnercentral_account.types.connection_type_detail

ConnectionTypeDetailMap: TypeAlias = dict[
    "aws_sdk_partnercentral_account.types.connection_type.ConnectionType",
    "aws_sdk_partnercentral_account.types.connection_type_detail.ConnectionTypeDetail",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ConnectionTypeDetailMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_partnercentral_account.types.connection_type
        import aws_sdk_partnercentral_account.types.connection_type_detail

        out[
            aws_sdk_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
                key
            )
        ] = aws_sdk_partnercentral_account.types.connection_type_detail.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeDetailMap:
    out: ConnectionTypeDetailMap = {}
    for key, value in data.items():
        import aws_sdk_partnercentral_account.types.connection_type
        import aws_sdk_partnercentral_account.types.connection_type_detail

        out[
            aws_sdk_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                key
            )
        ] = aws_sdk_partnercentral_account.types.connection_type_detail.deserialize_aws_json_1_0(
            value
        )
    return out
