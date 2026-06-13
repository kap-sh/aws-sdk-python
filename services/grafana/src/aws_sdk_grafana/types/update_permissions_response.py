"""Generated from Smithy shape ``com.amazonaws.grafana#UpdatePermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.update_error_list


class UpdatePermissionsResponse(TypedDict):
    errors: "aws_sdk_grafana.types.update_error_list.UpdateErrorList"
    """<p>An array of structures that contain the errors from the operation, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePermissionsResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.update_error_list

    out["errors"] = aws_sdk_grafana.types.update_error_list.serialize_json(
        value["errors"]
    )
    return out


def deserialize_json(data: dict) -> UpdatePermissionsResponse:
    out: UpdatePermissionsResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_grafana.types.update_error_list

        out["errors"] = aws_sdk_grafana.types.update_error_list.deserialize_json(
            data["errors"]
        )
    else:
        raise DeserializationError("UpdatePermissionsResponse.errors required")
    return out
