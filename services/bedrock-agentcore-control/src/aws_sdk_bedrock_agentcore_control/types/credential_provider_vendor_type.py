"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CredentialProviderVendorType``."""

import datetime
import decimal
from typing import AsyncIterator, Iterator, Literal, TypeAlias, cast
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError
from aws_sdk_bedrock_agentcore_control._protocol.xml import Element, SubElement
import base64
from email.utils import format_datetime as _fmt_http
from email.utils import parsedate_to_datetime as _parse_http

CredentialProviderVendorType: TypeAlias = Literal["GoogleOauth2", "GithubOauth2", "SlackOauth2", "SalesforceOauth2", "MicrosoftOauth2", "CustomOauth2", "AtlassianOauth2", "LinkedinOauth2", "XOauth2", "OktaOauth2", "OneLoginOauth2", "PingOneOauth2", "FacebookOauth2", "YandexOauth2", "RedditOauth2", "ZoomOauth2", "TwitchOauth2", "SpotifyOauth2", "DropboxOauth2", "NotionOauth2", "HubspotOauth2", "CyberArkOauth2", "FusionAuthOauth2", "Auth0Oauth2", "CognitoOauth2",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("GoogleOauth2", "GithubOauth2", "SlackOauth2", "SalesforceOauth2", "MicrosoftOauth2", "CustomOauth2", "AtlassianOauth2", "LinkedinOauth2", "XOauth2", "OktaOauth2", "OneLoginOauth2", "PingOneOauth2", "FacebookOauth2", "YandexOauth2", "RedditOauth2", "ZoomOauth2", "TwitchOauth2", "SpotifyOauth2", "DropboxOauth2", "NotionOauth2", "HubspotOauth2", "CyberArkOauth2", "FusionAuthOauth2", "Auth0Oauth2", "CognitoOauth2",))


def serialize_json(value: CredentialProviderVendorType) -> str:
    return value


def deserialize_json(data: str) -> CredentialProviderVendorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CredentialProviderVendorType value: {data!r}")
    return cast(CredentialProviderVendorType, data)