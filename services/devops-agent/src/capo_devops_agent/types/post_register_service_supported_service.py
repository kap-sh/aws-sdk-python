"""Generated from Smithy shape ``com.amazonaws.devopsagent#PostRegisterServiceSupportedService``."""

from typing import Literal, TypeAlias, cast

"""<p>Services that can be registered via the post-registration API (excludes OAuth 3LO services).</p>"""
PostRegisterServiceSupportedService: TypeAlias = Literal[
    "dynatrace",
    "servicenow",
    "pagerduty",
    "gitlab",
    "eventChannel",
    "mcpservernewrelic",
    "mcpservergrafana",
    "mcpserverdatadog",
    "mcpserver",
    "mcpserversplunk",
    "azureidentity",
    "mcpserversigv4",
]


# --- restJson1 ser/de ---
def serialize_json(value: PostRegisterServiceSupportedService) -> str:
    return value


def deserialize_json(data: str) -> PostRegisterServiceSupportedService:
    return cast(PostRegisterServiceSupportedService, data)
