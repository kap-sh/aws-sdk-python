"""Generated from Smithy shape ``com.amazonaws.kendra#AuthenticationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.basic_authentication_configuration_list


class AuthenticationConfiguration(TypedDict):
    basic_authentication: NotRequired[
        "aws_sdk_kendra.types.basic_authentication_configuration_list.BasicAuthenticationConfigurationList"
    ]
    """<p>The list of configuration information that's required to connect to and crawl a website host using basic authentication credentials.</p> <p>The list includes the name and port number of the website host.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationConfiguration) -> dict:
    out: dict = {}
    if "basic_authentication" in value:
        import aws_sdk_kendra.types.basic_authentication_configuration_list

        out["BasicAuthentication"] = (
            aws_sdk_kendra.types.basic_authentication_configuration_list.serialize_aws_json_1_1(
                value["basic_authentication"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthenticationConfiguration:
    out: AuthenticationConfiguration = {}  # type: ignore[typeddict-item]
    if "BasicAuthentication" in data:
        import aws_sdk_kendra.types.basic_authentication_configuration_list

        out["basic_authentication"] = (
            aws_sdk_kendra.types.basic_authentication_configuration_list.deserialize_aws_json_1_1(
                data["BasicAuthentication"]
            )
        )
    return out
