"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfRedshiftDataShares``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dataexchange.types.redshift_data_share_details

ListOfRedshiftDataShares: TypeAlias = list[
    "aws_sdk_dataexchange.types.redshift_data_share_details.RedshiftDataShareDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRedshiftDataShares) -> list:
    import aws_sdk_dataexchange.types.redshift_data_share_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_dataexchange.types.redshift_data_share_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfRedshiftDataShares:
    import aws_sdk_dataexchange.types.redshift_data_share_details

    out: ListOfRedshiftDataShares = []
    for item in data:
        out.append(
            aws_sdk_dataexchange.types.redshift_data_share_details.deserialize_json(
                item
            )
        )
    return out
