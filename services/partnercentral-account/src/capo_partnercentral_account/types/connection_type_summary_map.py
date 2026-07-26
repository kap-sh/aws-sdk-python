"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#ConnectionTypeSummaryMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_account.types.connection_type
    import capo_partnercentral_account.types.connection_type_summary

ConnectionTypeSummaryMap: TypeAlias = dict[
    "capo_partnercentral_account.types.connection_type.ConnectionType",
    "capo_partnercentral_account.types.connection_type_summary.ConnectionTypeSummary",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ConnectionTypeSummaryMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_partnercentral_account.types.connection_type
        import capo_partnercentral_account.types.connection_type_summary

        out[
            capo_partnercentral_account.types.connection_type.serialize_aws_json_1_0(
                key
            )
        ] = capo_partnercentral_account.types.connection_type_summary.serialize_aws_json_1_0(
            value
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ConnectionTypeSummaryMap:
    out: ConnectionTypeSummaryMap = {}
    for key, value in data.items():
        import capo_partnercentral_account.types.connection_type
        import capo_partnercentral_account.types.connection_type_summary

        out[
            capo_partnercentral_account.types.connection_type.deserialize_aws_json_1_0(
                key
            )
        ] = capo_partnercentral_account.types.connection_type_summary.deserialize_aws_json_1_0(
            value
        )
    return out
