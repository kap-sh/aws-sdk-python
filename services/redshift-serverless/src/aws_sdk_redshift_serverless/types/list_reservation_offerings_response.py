"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ListReservationOfferingsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.pagination_token
    import aws_sdk_redshift_serverless.types.reservation_offerings_list


class ListReservationOfferingsResponse(TypedDict, closed=True):
    reservation_offerings_list: "aws_sdk_redshift_serverless.types.reservation_offerings_list.ReservationOfferingsList"
    """<p>The returned list of reservation offerings.</p>"""
    next_token: NotRequired[
        "aws_sdk_redshift_serverless.types.pagination_token.PaginationToken"
    ]
    """<p>The token to use when requesting the next set of items.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListReservationOfferingsResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.reservation_offerings_list

    out["reservationOfferingsList"] = (
        aws_sdk_redshift_serverless.types.reservation_offerings_list.serialize_aws_json_1_1(
            value["reservation_offerings_list"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListReservationOfferingsResponse:
    out: ListReservationOfferingsResponse = {}  # type: ignore[typeddict-item]
    if "reservationOfferingsList" in data:
        import aws_sdk_redshift_serverless.types.reservation_offerings_list

        out["reservation_offerings_list"] = (
            aws_sdk_redshift_serverless.types.reservation_offerings_list.deserialize_aws_json_1_1(
                data["reservationOfferingsList"]
            )
        )
    else:
        raise DeserializationError(
            "ListReservationOfferingsResponse.reservation_offerings_list required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
