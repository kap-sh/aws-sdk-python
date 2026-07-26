"""Generated from Smithy shape ``com.amazonaws.dataexchange#ListOfRedshiftDataShares``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_dataexchange.types.redshift_data_share_details

ListOfRedshiftDataShares: TypeAlias = list[
    "capo_dataexchange.types.redshift_data_share_details.RedshiftDataShareDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfRedshiftDataShares) -> list:
    import capo_dataexchange.types.redshift_data_share_details

    out: list = []
    for item in value:
        out.append(
            capo_dataexchange.types.redshift_data_share_details.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ListOfRedshiftDataShares:
    import capo_dataexchange.types.redshift_data_share_details

    out: ListOfRedshiftDataShares = []
    for item in data:
        out.append(
            capo_dataexchange.types.redshift_data_share_details.deserialize_json(item)
        )
    return out
