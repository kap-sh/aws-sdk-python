"""Generated from Smithy shape ``com.amazonaws.chime#UpdateAccountRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.account_name
    import aws_sdk_chime.types.license
    import aws_sdk_chime.types.non_empty_string


class UpdateAccountRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    name: NotRequired["aws_sdk_chime.types.account_name.AccountName"]
    """<p>The new name for the specified Amazon Chime account.</p>"""
    default_license: NotRequired["aws_sdk_chime.types.license.License"]
    """<p>The default license applied when you add users to an Amazon Chime account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAccountRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "default_license" in value:
        import aws_sdk_chime.types.license

        out["DefaultLicense"] = aws_sdk_chime.types.license.serialize_json(
            value["default_license"]
        )
    return out


def deserialize_json(data: dict) -> UpdateAccountRequest:
    out: UpdateAccountRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "DefaultLicense" in data:
        import aws_sdk_chime.types.license

        out["default_license"] = aws_sdk_chime.types.license.deserialize_json(
            data["DefaultLicense"]
        )
    return out
