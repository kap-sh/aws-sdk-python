"""Generated from Smithy shape ``com.amazonaws.signin#CodeVerifier``."""

from typing import TypeAlias

"""PKCE code verifier for OAuth 2.0 security PKCE code verifier to prove possession of the original code challenge. Used to prevent authorization code interception attacks in public clients. Must be 43-128 characters using unreserved characters [A-Z] / [a-z] / [0-9] / \"-\" / \".\" / \"_\" / \"~\""""
CodeVerifier: TypeAlias = str
