"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListReservationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.reservations_list


class ListReservationsResponse(TypedDict):
    reservations_list: (
        "aws_sdk_redshift_serverless.types.reservations_list.ReservationsList"
    )
    """<p>The serverless reservations returned by the request.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReservationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.reservations_list

    out["reservationsList"] = (
        aws_sdk_redshift_serverless.types.reservations_list.serialize_aws_json_1_1(
            value["reservations_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReservationsResponse:
    out: ListReservationsResponse = {}  # type: ignore[typeddict-item]
    if "reservationsList" in data:
        import aws_sdk_redshift_serverless.types.reservations_list

        out["reservations_list"] = (
            aws_sdk_redshift_serverless.types.reservations_list.deserialize_aws_json_1_1(
                data["reservationsList"]
            )
        )
    else:
        raise DeserializationError(
            "ListReservationsResponse.reservations_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
