"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageTestsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_tests_timeout_minutes
    import capo_imagebuilder.types.nullable_boolean


class ImageTestsConfiguration(TypedDict, closed=True):
    image_tests_enabled: NotRequired[
        "capo_imagebuilder.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Determines if tests should run after building the image. Image Builder defaults to enable tests to run following the image build, before image distribution.</p>"""
    timeout_minutes: NotRequired[
        "capo_imagebuilder.types.image_tests_timeout_minutes.ImageTestsTimeoutMinutes"
    ]
    """<p>The maximum time in minutes that tests are permitted to run.</p> <note> <p>The timeout property is not currently active. This value is ignored.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageTestsConfiguration) -> dict:
    out: dict = {}
    if "image_tests_enabled" in value:
        out["imageTestsEnabled"] = value["image_tests_enabled"]
    if "timeout_minutes" in value:
        out["timeoutMinutes"] = value["timeout_minutes"]
    return out


def deserialize_json(data: dict) -> ImageTestsConfiguration:
    out: ImageTestsConfiguration = {}  # type: ignore[typeddict-item]
    if "imageTestsEnabled" in data:
        out["image_tests_enabled"] = data["imageTestsEnabled"]
    if "timeoutMinutes" in data:
        out["timeout_minutes"] = data["timeoutMinutes"]
    return out
