"""Generated from Smithy shape ``com.amazonaws.lakeformation#RedshiftConnect``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.service_authorization


class RedshiftConnect(TypedDict, closed=True):
    authorization: (
        "aws_sdk_lakeformation.types.service_authorization.ServiceAuthorization"
    )
    """<p>The authorization status for Redshift Connect. Valid values are ENABLED or DISABLED.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnect) -> dict:
    out: dict = {}
    import aws_sdk_lakeformation.types.service_authorization

    out["Authorization"] = (
        aws_sdk_lakeformation.types.service_authorization.serialize_json(
            value["authorization"]
        )
    )
    return out


def deserialize_json(data: dict) -> RedshiftConnect:
    out: RedshiftConnect = {}  # type: ignore[typeddict-item]
    if "Authorization" in data:
        import aws_sdk_lakeformation.types.service_authorization

        out["authorization"] = (
            aws_sdk_lakeformation.types.service_authorization.deserialize_json(
                data["Authorization"]
            )
        )
    else:
        raise DeserializationError("RedshiftConnect.authorization required")
    return out
